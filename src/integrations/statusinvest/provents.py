from ...base import get_webdriver, By
import pandas as pd
import numpy as np
import json
from datetime import date

def get_provents_df(ticker):
  driver = get_webdriver()
  driver.get(f'https://statusinvest.com.br/acoes/{ticker}')
  
  df = pd.DataFrame(json.loads(driver.find_element(By.XPATH, '//*[@id="results"]').get_attribute('value')))
  df['ed'] = pd.to_datetime(df['ed'], dayfirst=True)
  df['pd'] = pd.to_datetime(df['pd'], dayfirst=True, errors='coerce')
  
  driver.close()
  return df

def get_by_year_df(tickers):
  df_rows = []
  current_year = date.today().year

  for ticker in tickers:
    df_provents = get_provents_df(ticker)
    df_by_year = df_provents.groupby([df_provents.ed.dt.year]).sum('v').reset_index()
    provents_avg_3y = df_by_year[df_by_year['ed'].between(current_year-3,current_year-1)]['v'].sum() / 3 # 3 anos
    provents_avg_5y = df_by_year[df_by_year['ed'].between(current_year-5,current_year-1)]['v'].sum() / 5 # 5 anos

    df_rows.append([ticker, provents_avg_3y, provents_avg_5y])
  
  df = pd.DataFrame(np.array(df_rows), columns=['TICKER','PROVENTOS 3ANOS','PROVENTOS 5ANOS'])
  df[['PROVENTOS 3ANOS','PROVENTOS 5ANOS']] = df[['PROVENTOS 3ANOS','PROVENTOS 5ANOS']].astype(float)
  return df