import pandas as pd

pd.set_option('mode.use_inf_as_na', True)

def get_df_rank(df_stocks):
  df = df_stocks.copy()

  df['EY'] = df[' LPA'] / df['PRECO']
  df['RANK EY'] = df['EY'].rank(ascending=False)
  df['RANK ROE'] = df['ROE'].rank(ascending=False)
  df['RANK ROIC'] = df['ROIC'].rank(ascending=False)
  df['MF'] = df[['RANK EY','RANK ROE','RANK ROIC']].sum(axis=1)

  return pd.DataFrame(df[df['EY'].notnull() & df['ROE'].notnull() & df['ROIC'].notnull()], 
                      columns=['TICKER','EY','RANK EY','RANK ROE','RANK ROIC','MF'])