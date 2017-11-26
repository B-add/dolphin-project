import json

import requests

URL = 'https://dolphin.jump-technology.com:3389/api/v1/'
AUTH = ('epita_user_1', 'dolphin20412')


def get_portfolio():
    res = requests.get(URL + 'portfolio/564/dyn_amount_compo',
                       auth=AUTH,
                       verify=False)
    return res.content.decode('utf-8')


def set_portfolio(id):
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