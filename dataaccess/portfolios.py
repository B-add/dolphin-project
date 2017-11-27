import json

import requests

from dataaccess.assets import get_asset
from funcs import optimize_assets

URL = 'https://dolphin.jump-technology.com:3389/api/v1/'
AUTH = ('epita_user_1', 'dolphin20412')


def get_portfolio(id=564):
    res = requests.get(URL + 'portfolio/' + str(id) + '/dyn_amount_compo',
                       auth=AUTH,
                       verify=False)
    return json.loads(res.content.decode('utf-8'))


def set_portfolio(id=564):
    res = requests.get(URL + 'portfolio/' + str(id) + '/dyn_amount_compo',
                       auth=AUTH,
                       verify=False,
                       data=json.dumps({
                           'ratio': ratio_ids,
                           'asset': asset_ids,
                           'benchmark': benchmark,
                           'start_date': start_date,
                           'end_date': end_date,
                           'frequency': None
                        }))
    return res.content


def get_our_portfolio():
    res = requests.get(URL + 'asset?columns=ASSET_DATABASE_ID&columns=LABEL&columns=TYPE&TYPE=PORTFOLIO',
                       auth=AUTH,
                       verify=False)
    return res.content.decode('utf-8')


def set_test_portfolio():
    ids_weights = (optimize_assets(20, 100))
    ids = [item[0] for item in ids_weights]
    weights = [item[1] for item in ids_weights]
    print(ids)
    print(weights)
    assets = []
    money = 10000000
    for i, id in enumerate(ids):
        val = float(json.loads(get_asset(id=id, full_response=False, columns=["LAST_CLOSE_VALUE"],
                  date="2011-12-31"))["LAST_CLOSE_VALUE"]["value"].split()[0].replace(',', '.'))
        tmp = money * weights[i]
        q = tmp / val
        assets.append({'asset': {'asset': id, 'quantity': int(q)}})
    result = {'currency': {'code': 'EUR'},
              'label': 'PORTFOLIO_USER1',
              'type': 'front',
              'values': {'2012-01-01':  assets}}
    print(result)