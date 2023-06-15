import requests
import json
from config import keys

class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        try:
            quote_ticker = keys[quote]
        except:
            raise APIException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except:
            raise APIException(f'Не удалось обработать число {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = amount * json.loads(r.content)[keys[base]]
        return total_base

