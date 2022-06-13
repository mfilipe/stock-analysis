import pandas as pd
import numpy as np

def get_by_dy_df(tickers, df_provents, df_stocks):
  df_rows = []

  for ticker in tickers:
    provents_1y = df_provents[df_provents['TICKER'] == ticker]['PROVENTOS 1 ANO'].iat[0]
    provents_5y = df_provents[df_provents['TICKER'] == ticker]['PROVENTOS 5 ANOS'].iat[0]

    highest_price = lambda provents, dy: provents / (dy / 100)
    
    df_rows.append([ticker, highest_price(provents_1y, df_stocks[df_stocks['TICKER'] == ticker]['DY'].iat[0]), 
                    highest_price(provents_5y, 5), highest_price(provents_5y, 10)])
  
  return pd.DataFrame(np.array(df_rows), columns=['TICKER','PRECO-TETO DY ATUAL','PRECO-TETO DY 5%',
                                                  'PRECO-TETO DY 10%'])