from datetime import date
import pandas as pd
import requests
import jmespath

def get_last_year_balance_df(tickers):
  last_year = date.today().year-1
  records = []
  for ticker in tickers:
    data = requests.get(
      url=f'https://statusinvest.com.br/acao/getativos?code={ticker}&type=0&futureData=false&range.min={last_year}&range.max={last_year}'
    ).json()
    balance_values = {x[0]: x[1] for x in jmespath.search('data.grid[*].gridLineModel.[key, values[0]]', data)}
    passive = balance_values['PassivoCiruclante'] + balance_values['PassivoNaoCiruclante']
    records.append({
      'TICKER': ticker, 
      'ATIVO': balance_values['AtivoTotal'],
      'PASSIVO': passive,
      'PATRIMONIO LÍQUIDO': balance_values['PatrimonioLiquidoConsolidado'],
      'P. LIQ. / PASSIVO': balance_values['PatrimonioLiquidoConsolidado'] / passive
    } | balance_values)

  return pd.DataFrame.from_records(records)