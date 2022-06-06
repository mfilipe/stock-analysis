import pandas as pd

def get_df(df_stocks):
  df = df_stocks.copy()

  df['EY'] = df[' LPA'] / df['PRECO']
  df['RANK EY'] = df['EY'].rank(ascending=False)
  df['RANK ROIC'] = df['ROIC'].rank(ascending=False)
  df['MF'] = df[['RANK EY','RANK ROIC']].sum(axis=1)

  return pd.DataFrame(df, columns=['TICKER','EY','RANK EY','RANK ROIC','MF'])