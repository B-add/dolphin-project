import requests

URL = 'https://dolphin.jump-technology.com:3389/api/v1/'
AUTH = ('epita_user_1', 'dolphin20412')


def get_ratios():
    res = requests.get(URL + 'ratio',
                       auth=AUTH,
                       verify=False)
    return res.content