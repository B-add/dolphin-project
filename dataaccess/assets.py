import requests

URL = 'https://dolphin.jump-technology.com:3389/api/v1/'


def get_assets():
    res = requests.get(URL + 'asset?columns=ASSET_DATABASE_ID&columns=LABEL&columns=TYPE&TYPE=PORTFOLIO',
                       auth=('epita_user_1', 'dolphin20412'),
                       verify=False)
    print(res.content)