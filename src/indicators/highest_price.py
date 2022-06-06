import pandas as pd
import numpy as np

def get_by_dividendyield_df(tickers, df_provents, df_stocks):
  df_rows = []

  for ticker in tickers:
    earnings_avg = df_provents[df_provents['TICKER'] == ticker]['PROVENTOS AVG 3A'].iat[0]
    highest_price_by_dy = lambda dy: earnings_avg / (dy / 100)
    
    df_rows.append([ticker, highest_price_by_dy(df_stocks[df_stocks['TICKER'] == ticker]['DY'].iat[0]), 
                    highest_price_by_dy(5), highest_price_by_dy(10)])
  
  return pd.DataFrame(np.array(df_rows), columns=['TICKER','PRECO-TETO DY ATUAL','PRECO-TETO DY 5%',
                                                  'PRECO-TETO DY 10%'])