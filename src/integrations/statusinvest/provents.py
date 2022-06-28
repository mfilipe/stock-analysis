from ...base import get_webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import json

def get_provents_df(ticker):
  driver = get_webdriver()
  driver.get(f'https://statusinvest.com.br/acoes/{ticker}')
  
  df = pd.DataFrame(json.loads(driver.find_element(By.XPATH, '//*[@id="results"]').get_attribute('value')))
  df['ed'] = pd.to_datetime(df['ed'], dayfirst=True)
  df['pd'] = pd.to_datetime(df['pd'], dayfirst=True, errors='coerce')
  
  driver.close()
  return df

def get_average_per_year_df(tickers):
  df_rows = []

  for ticker in tickers:
    df_provents = get_provents_df(ticker).sort_values('ed', ascending=True).set_index('ed')
    provents_1y = df_provents.last('12M')['v'].sum() # 1 ano
    provents_3y = df_provents.last('36M')['v'].sum() / 3 # 3 anos
    provents_5y = df_provents.last('60M')['v'].sum() / 5 # 5 anos

    df_rows.append([ticker, provents_1y, provents_3y, provents_5y])

  df = pd.DataFrame(np.array(df_rows), columns=['TICKER','PROVENTOS 1 ANO','PROVENTOS 3 ANOS','PROVENTOS 5 ANOS'])
  df[['PROVENTOS 1 ANO','PROVENTOS 3 ANOS','PROVENTOS 5 ANOS']] = df[['PROVENTOS 1 ANO','PROVENTOS 3 ANOS',
                                                                      'PROVENTOS 5 ANOS']].astype(float)
  return df