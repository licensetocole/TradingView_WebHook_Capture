import kucoin.client as kuclinet
from .api_creds import *

order_ids=[]

def order(side, quantity, symbol):
    client = kuclinet.Client(KU_API_PUBLIC, KU_API_SECRET, KU_PASSPHRASE)
    fixed_symbol = eth_tick_fix(symbol)
    try:
        print('\nSending order!')
        order = client.create_market_order(fixed_symbol, side, quantity)
        print(order)
        order_ids.append(order)
    except Exception as e:
        print('Failed to place order')
        print(e.__cause__)
        return (False, str(e.__cause__))
    return (True, order)

def eth_tick_fix(eth_ticker):
    if 'ETH' in eth_ticker:
        return 'ETH-USDT'
    return 'WRONG'

if __name__=='__main__':
    order('buy', .01, 'ETH-USDT' )
