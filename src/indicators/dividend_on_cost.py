import pandas as pd

def get_df_by_dy(tickers, df_stocks, df_dividends):
  records = []
  for ticker in tickers:
    df = df_dividends[df_dividends['TICKER'] == ticker]
    dividend_on_cost = lambda provents: provents * 100 / df_stocks[df_stocks['TICKER'] == ticker]['PRECO'].iat[0]
    records.append({
      'TICKER': ticker,
      'DY-ON-COST ATUAL': dividend_on_cost(df['PROVENTOS 1 ANO'].iat[0]),
      'DY-ON-COST 5 ANOS': dividend_on_cost(df['PROVENTOS 5 ANOS'].iat[0])
    })

  return pd.DataFrame(records)
