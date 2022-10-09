import ccxt
import time

exchange = ccxt.binance({
    'apikey' : 'stringaCorta', /*serve per la registrazione*/
    'secret' : 'password',
    'enableRateLimit': True
})
Prezzo_Attuale = exchange.fetchTicker('BTC/USDT')['last']
def quanto_in_dollari(cosa, quanto):
    return quanto/exchange.fetch_ticker(cosa+'/USDT')['last']
    

Market_order= exchange.create_market_buy_order('BTC/USDT',1)