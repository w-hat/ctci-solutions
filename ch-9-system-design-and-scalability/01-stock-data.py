# Design a system to deliver stock data.

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config

class Database(object):
  def __init__(self):
    self.stock_quotes = {
      "GOOG": {"open": 908.1, "close": 921.0, "low": 905.3, "high": 921.7},
      "AMZN": {"open": 812.7, "close": 817.1, "low": 812.5, "high": 818.5},
      "BIDU": {"open": 173.7, "close": 180.2, "low": 173.5, "high": 181.2},
      "INTC": {"open":  38.3, "close":  41.1, "low":  38.0, "high":  41.2},
      "NVDA": {"open": 112.8, "close": 116.8, "low": 111.9, "high": 117.0},
      "AAPL": {"open": 144.5, "close": 146.8, "low": 144.0, "high": 147.0},
      "SNAP": {"open":  24.9, "close":  27.0, "low":  24.0, "high":  25.2},
      "TWTR": {"open":  16.6, "close":  17.7, "low":  16.4, "high":  17.8},
      "IBM":  {"open": 168.6, "close": 171.1, "low": 168.4, "high": 172.1},
      "FB":   {"open": 140.2, "close": 148.3, "low": 140.2, "high": 150.3},
      "GE":   {"open":  32.2, "close":  31.4, "low":  32.0, "high":  32.8}}

db = Database()

@view_config(route_name='stock_quotes', renderer='json')
def stock_quotes(request):
  if 'tickers' in request.params:
    tickers = request.params['tickers'].split(',')
    quotes = {}
    for ticker in tickers:
      quotes[ticker] = db.stock_quotes[ticker]
    return quotes
  else:
    return db.stock_quotes

if __name__ == '__main__':
  config = Configurator()
  config.add_route('stock_quotes', '/stock_quotes')
  config.scan()
  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 8080, app)
  server.serve_forever()

