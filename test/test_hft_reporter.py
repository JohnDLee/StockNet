import sys
sys.path.append('../src/')
from StockMarketEndpoint import *
import sys
import signal
import time

if __name__ == '__main__':
    
    # init stock market endpoint
    sm = StockMarketEndpoint(name=sys.argv[1], username=sys.argv[2], password=sys.argv[2])
    sm.register(registered_ok=True)
    
    while True:
        # measure buy operations
        start = time.time_ns()
        sm.buy('TSLA', 10)
        end = time.time_ns()
        print( end - start)
        # sell
        sm.sell('TSLA', 10)