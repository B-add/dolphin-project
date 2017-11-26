import json

import requests

URL = 'https://dolphin.jump-technology.com:3389/api/v1/'
AUTH = ('epita_user_1', 'dolphin20412')


def get_ratios():
    """
    Get the available ratios

    :return: The available ratios to use in compute ratios
    """
    res = requests.get(URL + 'ratio',
                       auth=AUTH,
                       verify=False)
    return res.content


def compute_ratios(ratio_ids, asset_ids, benchmark=None, start_date=None, end_date=None):
    """
    Compute the given ratios for the given assets

    :param ratio_ids: The ratios array to compute
    :param asset_ids: The asset to compute the ratios from
    :param benchmark: The benchmark ?
    :param start_date: The date to start computation at
    :param end_date: The date to end computation at
    :return: The ratios results
    """
    res = requests.post(URL + 'ratio/invoke',
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
