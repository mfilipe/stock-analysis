from ...base import get_webdriver, By
import pandas as pd
import numpy as np
import json
from datetime import date

def get_dividends_df(ticker):
  driver = get_webdriver()
  driver.get(f'https://statusinvest.com.br/acoes/{ticker}')
  
  df = pd.DataFrame(json.loads(driver.find_element(By.XPATH, '//*[@id="results"]').get_attribute('value')))
  df['ed'] = pd.to_datetime(df['ed'], dayfirst=True)
  df['pd'] = pd.to_datetime(df['pd'], dayfirst=True, errors='coerce')
  
  driver.close()
  return df

def get_provents_by_year_df(tickers):
  df_rows = []
  current_year = date.today().year

  for ticker in tickers:
    df_dividends = get_dividends_df(ticker)
    df_earnings = df_dividends.groupby([df_dividends.ed.dt.year]).sum('v').reset_index()
    earnings_avg_3a = df_earnings[df_earnings['ed'].between(current_year-3,current_year-1)]['v'].sum() / 3 # 3 anos
    earnings_avg_5a = df_earnings[df_earnings['ed'].between(current_year-5,current_year-1)]['v'].sum() / 5 # 5 anos

    df_rows.append([ticker, earnings_avg_3a, earnings_avg_5a])
  
  df = pd.DataFrame(np.array(df_rows), columns=['TICKER','PROVENTOS 3ANOS','PROVENTOS 5ANOS'])
  df[['PROVENTOS 3ANOS','PROVENTOS 5ANOS']] = df[['PROVENTOS 3ANOS','PROVENTOS 5ANOS']].astype(float)
  return df