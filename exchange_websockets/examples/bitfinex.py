import logging
import time
import sys

from exchange_websockets.bitfinex.connection import WebSocketConnection

from exchange_websockets.bitfinex.client import BtfxWss

log = logging.getLogger(__name__)

# fh = logging.FileHandler('test.log')
# fh.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)

log.addHandler(sh)
# log.addHandler(fh)
# logging.basicConfig(level=logging.DEBUG, handlers=[fh, sh])
logging.basicConfig(level=logging.DEBUG, handlers=[sh])

wss = BtfxWss()
wss.start()

while not wss.conn.connected.is_set():
    time.sleep(1)

# Subscribe to some channels
wss.subscribe_to_ticker('BTCUSD')
wss.subscribe_to_order_book('BTCUSD')

# Do something else
# grasp vivify wolf legume nicety foyer entire
t = time.time()
while time.time() - t < 10:
    pass

# Accessing data stored in BtfxWss:
ticker_q = wss.tickers()  # returns a Queue object for the pair.
while not ticker_q.empty():
    print(ticker_q.get())

# Unsubscribing from channels:
wss.unsubscribe_from_ticker('BTCUSD')
wss.unsubscribe_from_order_book('BTCUSD')

# Shutting down the client:
wss.stop()