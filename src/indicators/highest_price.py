import pandas as pd
import numpy as np

def get_df_by_dy(tickers, df_dividends):
  highest_price = lambda provents, dy: provents / (dy / 100)
  
  records = []
  for ticker in tickers:
    df = df_dividends[df_dividends['TICKER'] == ticker]
    records.append({
      'TICKER': ticker,
      'PRECO-TETO DY ATUAL': highest_price(df['PROVENTOS 1 ANO'].iat[0], df['DY 1 ANO'].iat[0]),
      'PRECO-TETO DY 5 ANOS': highest_price(df['PROVENTOS 5 ANOS'].iat[0], df['DY 5 ANOS'].iat[0]),
      'PRECO-TETO DY 5%': highest_price(df['PROVENTOS 5 ANOS'].iat[0], 5),
      'PRECO-TETO DY 10%': highest_price(df['PROVENTOS 5 ANOS'].iat[0], 10)
    })
  
  return pd.DataFrame(records)