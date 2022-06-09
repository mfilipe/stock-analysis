from src.base import logging
import sys

if not (TICKERS := sys.argv[1:]):
  logging.error('Informe ao menos um ticker')
  sys.exit(1)

import src.integrations.statusinvest.stocks as statusinvest_stocks
import src.integrations.statusinvest.provents as statusinvest_provents
import src.integrations.statusinvest.payouts as statusinvest_payouts
import src.integrations.statusinvest.balance_sheet as statusinvest_balance_sheet
import src.indicators.magic_formula as magic_formula
import src.indicators.highest_price as highest_price
import src.output as output

df_stocks = statusinvest_stocks.get_all_df()
df_provents = statusinvest_provents.get_by_year_df(TICKERS)
df_payouts = statusinvest_payouts.get_by_year_df(TICKERS)
df_balance_sheet = statusinvest_balance_sheet.get_last_year_balance_df(TICKERS)
df_magic_formula = magic_formula.get_rank_df(df_stocks)
df_highest_price = highest_price.get_by_dy_df(TICKERS, df_provents, df_stocks)

output.get_formatted_df(df_stocks.join(df_provents.set_index('TICKER'), on='TICKER')
                                 .join(df_payouts.set_index('TICKER'), on='TICKER')
                                 .join(df_balance_sheet.set_index('TICKER'), on='TICKER')
                                 .join(df_magic_formula.set_index('TICKER'), on='TICKER')
                                 .join(df_highest_price.set_index('TICKER'), on='TICKER')).to_csv('output.csv')
sys.exit(0)