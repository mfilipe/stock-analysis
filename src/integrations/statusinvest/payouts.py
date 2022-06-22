import pandas as pd
import requests

def get_df_by_year(tickers):
  records = []
  for ticker in tickers:
    data = requests.get(url=f'https://statusinvest.com.br/acao/payoutresult?code={ticker}&type=1').json()['chart']
    records.append({
      f'PAYOUT {year}': data['series']['proventos'][index]['value'] / data['series']['lucroLiquido'][index]['value'] 
      for index, year in enumerate(data['category'])
    } | {'TICKER': ticker})

  return pd.DataFrame.from_records(records)