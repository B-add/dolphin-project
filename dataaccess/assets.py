import requests

URL = 'https://dolphin.jump-technology.com:3389/api/v1/'
AUTH = ('epita_user_1', 'dolphin20412')


def get_assets():
    res = requests.get(URL + 'asset',
                       auth=AUTH,
                       verify=False)
    return res.content


def get_asset(id):
    res = requests.get(URL + 'asset/' + str(id),
                       auth=AUTH,
                       verify=False)
    return res.content


def get_asset_attribute(id, attribute):
    res = requests.get(URL + 'asset/' + str(id) + '/attribute/' + attribute,
                       auth=AUTH,
                       verify=False)
    return res.content
