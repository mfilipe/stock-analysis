from ...base import get_webdriver
from selenium.webdriver.common.by import By
import src.integrations.investing.stocks as investing_stocks
import pandas as pd
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

def get_df_all(ticker):
  df_stocks = investing_stocks.get_all()

  tag = df_stocks[(df_stocks['country'] == 'brazil') & (df_stocks['symbol'].str.upper() == ticker)]['tag'].iat[0]
  driver = get_webdriver()
  driver.set_page_load_timeout(5)
  try:
    driver.get(f'https://www.investing.com/equities/{tag}-dividends')
  except TimeoutException:
    driver.execute_script("window.stop();")
  
  table = driver.find_element(By.XPATH, "//*[@tablesorter_dividends]")
  
  # solicitando todos os registros através do js
  pair_id = table.get_attribute('id').replace('dividendsHistoryData', '')
  get_last_timestamp = lambda: table.find_elements(By.XPATH, 'tbody/tr')[-1].get_attribute('event_timestamp')
  while True:
    last_timestamp = get_last_timestamp()
    driver.execute_script(f'showMoreDividendsHistory("{pair_id}", "");')
    WebDriverWait(driver, 20).until(lambda driver: driver.execute_script("return jQuery.active == 0"))
    if last_timestamp == get_last_timestamp():
      break

  records = []
  for tr in table.find_elements(By.XPATH, "tbody/tr"):
    tds = tr.find_elements(By.TAG_NAME, 'td')
    field_dy = tds[4].text.replace('%', '').replace(',', '')
    field_provents = tds[1].text
    field_payment = tds[3].text
    records.append({
      'TICKER': ticker,
      'DATA EX': datetime.strptime(tds[0].text, '%b %d, %Y'),
      'DATA PAGAMENTO': None if field_payment == '--' else datetime.strptime(field_payment, '%b %d, %Y'),
      'PROVENTOS': float(field_provents) if field_provents else None,
      'DY': None if field_dy == '-' else float(field_dy)
    }) 

  driver.close()

  return pd.DataFrame(records)

def get_df_average_by_period(tickers):
  records = []
  for ticker in tickers:
    df = get_df_all(ticker).sort_values('DATA EX', ascending=True).set_index('DATA EX')
    records.append({
      'TICKER': ticker,
      'PROVENTOS 1 ANO': df.last('12M')['PROVENTOS'].sum(),
      'PROVENTOS 3 ANOS': df.last('36M')['PROVENTOS'].sum() / 3,
      'PROVENTOS 5 ANOS': df.last('60M')['PROVENTOS'].sum() / 5,
      'DY 1 ANO': df.last('12M')['DY'].mean(),
      'DY 3 ANOS': df.last('36M').groupby(pd.Grouper(freq='12MS'))['DY'].mean().sum() / 3,
      'DY 5 ANOS': df.last('60M').groupby(pd.Grouper(freq='12MS'))['DY'].mean().sum() / 5
    } | {
      f'DY {date.year}': dy 
      for date, dy in df.groupby(pd.Grouper(freq='Y'))['DY'].mean().tail(6).iteritems()
    })
    
  return pd.DataFrame(records)
