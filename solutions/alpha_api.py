import argparse
import logging
import redis
import warnings
import pandas as pd
import matplotlib.pyplot as plt


from alpha_vantage.techindicators import TechIndicators

warnings.simplefilter(action='ignore', category=FutureWarning)


def plot_sma_for_tickers(data, keys):
    for key in keys:
        data[key]['SMA'].plot(label=key)


def get_sma_for_tickers(
        tickers, redis_conn=None, interval="daily", time_period=50, flush_redis=False,
        start_date="2019-01-01", end_date="2019-08-15"):

    ti = TechIndicators(output_format="pandas")
    data, meta_data = {}, {}
    keys = []
    for ticker in tickers:
        key = f"{ticker}:sma:{time_period}:{interval}"
        if redis_conn is None or flush_redis or not redis_conn.exists(key):
            # get from API
            data[key], meta_data[ticker] = ti.get_sma(symbol=ticker, time_period=time_period, interval=interval)
            data[key] = data[key].loc[start_date:end_date]  # time to data from this date
            if redis_conn is None:
                logging.warning("No redis connection, using API")
            else:
                if flush_redis:
                    logging.warning("Flushing old redis values, using API")
                elif not redis_conn.exists(key):
                    logging.warning("Cache miss, using API")
                redis_conn.set(key, data[key].to_msgpack(compress='zlib'))
        else:
            # get from redis
            logging.warning(f"Grabbing {key} from redis")
            data[key] = pd.read_msgpack(redis_conn.get(key))

        keys.append(key)

    return data, keys


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tickers", help="list of stock ticker you want to chart")
    parser.add_argument("-f", "--flush", action="store_true", help="flush redis cache")
    parser.add_argument("-nr", "--no_redis", action="store_true", help="don't use redis")
    parser.add_argument("-i", "--interval", default="daily", help="size of interval")
    parser.add_argument("-t", "--time_period", default=50, help="time_period")

    args = parser.parse_args()
    logging.warning(f"Command line arguments are: {args}")
    my_tickers = [ticker.strip() for ticker in args.tickers.split(",")]
    my_flush_redis = False
    if args.flush:
        my_flush_redis = True
    my_interval = "daily"
    if args.interval:
        my_interval = args.interval
    my_redis_conn = None
    if not args.no_redis:
        my_redis_conn = redis.Redis(host="localhost", port=6379, db=0)
    my_data, my_keys = get_sma_for_tickers(
        my_tickers, redis_conn=my_redis_conn, flush_redis=my_flush_redis,
        interval=my_interval, time_period=args.time_period)
    plot_sma_for_tickers(my_data, my_keys)
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.title(f'Using a mixture of Redis and the Alpha Vantage API')
    plt.show()

"""
EXAMPLE command line usage:
$ python -m alpha_api "GOOG, NFLX" -i="weekly" -t 50 --no_redis

Namespace(flush=False, interval='weekly', no_redis=True, tickers='GOOG, NFLX', time_period='50')
WARNING:root:No redis connection, using API
WARNING:root:No redis connection, using API
"""


