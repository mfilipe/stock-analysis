import pandas as pd
from datetime import date

def get_formatted_df(df_full):
  current_year = date.today().year
  return pd.DataFrame(df_full, 
                      columns=['TICKER','PRECO','P/L','DIVIDA LIQUIDA / EBIT','P. LIQ. / PASSIVO',
                               'ROE','ROIC',' LPA','EY','RANK EY','RANK ROE','RANK ROIC','MF',
                               'CAGR RECEITAS 5 ANOS','CAGR LUCROS 5 ANOS',
                               'PROVENTOS 1 ANO','PROVENTOS 5 ANOS','DY 1 ANO','DY 5 ANOS',
                               'PRECO-TETO DY ATUAL','PRECO-TETO DY 5 ANOS','PRECO-TETO DY 5%','PRECO-TETO DY 10%'] +
                              [f'PAYOUT {year}' for year in range(current_year, current_year-6, -1)] +
                              [f'DY {year}' for year in range(current_year, current_year-6, -1)] +
                              ['ATIVO','PASSIVO','PATRIMONIO LÍQUIDO']).set_index('TICKER') \
                                                                       .sort_values('MF', ascending=True)