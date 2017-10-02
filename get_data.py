# Alpha Vantage API Key: 4BWQGJ75VET4DK8I
# Document: https://www.alphavantage.co/documentation/
# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=MSFT&outputsize=full&apikey=4BWQGJ75VET4DK8I

# Tiingo
# https://api.tiingo.com/docs/tiingo/daily#priceData
# https://api.tiingo.com/services/tiingo/daily
# Auth Token: bf4f408337a25e48b67fdc365ae25476c3fba483
# https://api.tiingo.com/tiingo/daily/googl/prices?startDate=2016-1-1&endDate=2017-1-1&token=bf4f408337a25e48b67fdc365ae25476c3fba48
# pd.read_json("https://api.tiingo.com/tiingo/daily/googl/prices?startDate=2016-1-1&endDate=2017-1-1&token=bf4f408337a25e48b67fdc365ae25476c3fba483")

# https://stooq.com
# Where should I get API?

# http://quant.caltech.edu/historical-stock-data.html

import pandas as pd
import argparse
import arrow
from os import mkdir
from os import path
import shutil


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-SD', '--start_date', type=str,
                        default='2000-01-01', help='Start date parameter value - format YYYY-MM-DD')
    parser.add_argument('-ED', '--end_date', type=str,
                        default=arrow.now().format('YYYY-MM-DD'), help='End date parameter - format YYYY-MM-DD')
    parser.add_argument('-TI', '--ticker', nargs='+',
                        help='<Required> Set flag')
    parser.add_argument('-TL', '--tickerfile')
    parser.add_argument('-T', '--type', type=str,
                        help='type of stock, ex: ETF')
    args = parser.parse_args()
    # # fetch all data
    if args.ticker is not None:
        for ticker in set(args.ticker):
            ticker_dir = "data/{}".format(ticker)
            type_dir = "data/{}".format(args.type)
            if not path.exists(ticker_dir):
                mkdir(ticker_dir)
            if not path.exists(type_dir):
                mkdir(type_dir)
            fetch_tiingo_data(ticker, args.start_date, args.end_date,
                              "data/{}/{}.csv".format(ticker, ticker))
            shutil.copy("data/{}/{}.csv".format(ticker, ticker), type_dir)
    if args.tickerfile is not None:
        arr = open(args.tickerfile).read().split("\n")
        # print(arr)
        for ticker in arr:
            if ticker != '':
                ticker_dir = "data/{}".format(ticker)
                type_dir = "data/{}".format(args.type)
                if not path.exists(ticker_dir):
                    print("grabbing {} for you, my lord".format(ticker))
                    mkdir(ticker_dir)
                    fetch_tiingo_data(
                        ticker, args.start_date, args.end_date, "data/{}/{}.csv".format(ticker, ticker))
                    if not path.exists(type_dir):
                        mkdir(type_dir)
                    shutil.copy(
                        "data/{}/{}.csv".format(ticker, ticker), type_dir)
                else:
                    print("You already have {}, my lord".format(ticker))


def fetch_tiingo_data(ticker, start_date, end_date, fname):
    url = "https://api.tiingo.com/tiingo/daily/{ticker}/prices?startDate={start_date}&endDate={end_date}&token={token}"
    token = "ca5a6f47a99ae61051e4de63b26f727b1709a01d"
    data = pd.read_json(url.format(
        ticker=ticker,
        start_date=start_date,
        end_date=end_date,
        token=token
    ))
    data.to_csv(fname, columns=["date", "open", "high",
                                "low", "close", "volume"], index=False, header=False)


if __name__ == '__main__':
    main()
