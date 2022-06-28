import sys

if not (TICKERS := list(map(str.upper, sys.argv[1:]))):
  raise ValueError('Informe ao menos um ticker')

import src.integrations.statusinvest.stocks as statusinvest_stocks
# import src.integrations.statusinvest.provents as statusinvest_provents
import src.integrations.investing.dividends as investing_dividends
import src.integrations.statusinvest.payouts as statusinvest_payouts
import src.integrations.statusinvest.balance_sheet as statusinvest_balance_sheet
import src.indicators.magic_formula as magic_formula
import src.indicators.highest_price as highest_price
import src.output as output

df_stocks = statusinvest_stocks.get_df_all()
df_dividends = investing_dividends.get_df_average_by_period(TICKERS)
df_payouts = statusinvest_payouts.get_df_by_year(TICKERS)
df_balance_sheet = statusinvest_balance_sheet.get_df_last_year(TICKERS)
df_magic_formula = magic_formula.get_df_rank(df_stocks)
df_highest_price = highest_price.get_df_by_dy(TICKERS, df_dividends)

output.get_formatted_df(df_stocks.join(df_dividends.set_index('TICKER'), on='TICKER')
                                 .join(df_payouts.set_index('TICKER'), on='TICKER')
                                 .join(df_balance_sheet.set_index('TICKER'), on='TICKER')
                                 .join(df_magic_formula.set_index('TICKER'), on='TICKER')
                                 .join(df_highest_price.set_index('TICKER'), on='TICKER')).to_csv('output.csv')
sys.exit(0)