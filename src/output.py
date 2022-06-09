import pandas as pd

def get_formatted_df(df_full):
  return pd.DataFrame(df_full, 
                      columns=['TICKER','PRECO','P/L','DIVIDA LIQUIDA / EBIT','P. LIQ. / PASSIVO','ROE','ROIC',' LPA',
                               'EY','RANK EY','RANK ROIC','MF',
                               'PROVENTOS 3ANOS','PROVENTOS 5ANOS',
                               'DY','PRECO-TETO DY ATUAL','PRECO-TETO DY 5%','PRECO-TETO DY 10%',
                               'PAYOUT 2021','PAYOUT 2020','PAYOUT 2019','PAYOUT 2018','PAYOUT 2017',
                               'ATIVO','PASSIVO','PATRIMONIO LÍQUIDO']).set_index('TICKER') \
                                                                       .sort_values('MF', ascending=True)