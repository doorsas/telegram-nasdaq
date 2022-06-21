import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials

# yahoo_financials = YahooFinancials('BTC-USD')
# data=yahoo_financials.get_historical_price_data("2019-07-10", "2021-05-30", "monthly")
# btc_df = pd.DataFrame(data['BTC-USD']['prices'])
# btc_df = btc_df.drop('date', axis=1).set_index('formatted_date')
# print (btc_df.sample(20))

TICKERSS = ('VOW3.DE', 'T')

for ticker in TICKERSS:
    aapl_sausis = yf.download(ticker,
                          start='2022-01-05',
                          end='2022-01-05',
                          progress=False,
    )
    print ('va tau 01 04  ',ticker, aapl_sausis['Close'][0])


    aapl_geguze = yf.download(ticker,
                          start='2022-06-02',
                          end='2022-06-02',
                          progress=False,
    )
    print ('va tau 06 02', ticker, aapl_geguze['Close'][0])







# for a in TICKERSS:
#     # aapl_historical = aapl.history(start="2020-06-02", end="2020-06-07", interval="1m")
#     ticker = yf.Ticker(a)
#     aapl_df = ticker.history(period="10y")
#     aapl_df['Close'].plot(title="APPLE's stock price")
#
#     # aapl_major_holders = ticker.major_holders
#     # aapl_holders = ticker.institutional_holders
#     # aapl_actions = ticker.actions
#     aapl_price = ticker.info['regularMarketPrice']
#
#
#     # print (aapl_holders)
#     # print (aapl_major_holders)
#     # print (aapl_actions)
#     print (a, aapl_price)
