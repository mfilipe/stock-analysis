import pandas as pd
from ...base import make_request

def get_df_by_year(tickers):
  records = []
  for ticker in tickers:
    data = make_request(f'https://statusinvest.com.br/acao/payoutresult?code={ticker}&type=1').json()['chart']
    records.append({
      f'PAYOUT {year}': data['series']['proventos'][index]['value'] / data['series']['lucroLiquido'][index]['value'] 
      for index, year in enumerate(data['category'])
    } | {'TICKER': ticker})

  return pd.DataFrame.from_records(records)