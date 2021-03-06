import json

import requests

URL = 'https://dolphin.jump-technology.com:3389/api/v1/'
AUTH = ('epita_user_1', 'dolphin20412')


def get_assets(date=None, full_response=False, columns=list()):
    """
    Get the asset list

    :param date: The date for the assets we want
    :param full_response: Boolean to include null columns
    :param columns: String array containing the wanted columns
    :return: The assets matching the parameters
    """
    payload = {'date': date, 'fullResponse': full_response }
    res = requests.get(URL + 'asset' + columns_to_str(columns),
                       params=payload,
                       auth=AUTH,
                       verify=False)
    return res.content.decode('utf-8')


def get_asset(id, date=None, full_response=True, columns=list()):
    """
    Get the asset matching the given id

    :param date: The date for the asset we want
    :param id: The wanted asset's id
    :param full_response: Boolean to include null columns
    :param columns: String array containing the wanted columns
    :return: The wanted asset and columns
    """
    payload = {'date': date, 'fullResponse': full_response}
    toto = URL + 'asset/' + str(id) + columns_to_str(columns)
    print(toto)
    res = requests.get(toto,
                       params=payload,
                       auth=AUTH,
                       verify=False)
    return res.content.decode('utf-8')


def get_asset_attribute(id, attribute):
    """
    Get a specific attribute from an asset
    
    :param id: The id of the asset we want the attribute from
    :param attribute: The wanted attribute
    :return: The value matching the asset's attribute
    """
    res = requests.get(URL + 'asset/' + str(id) + '/attribute/' + attribute,
                       auth=AUTH,
                       verify=False)
    return res.content.decode('utf-8')


def get_asset_quotes(id, start_date, end_date):
    payload = {'start_date': start_date, 'end_date': end_date}
    res = requests.get(URL + 'asset/' + str(id) + '/quote',
                       params=payload,
                       auth=AUTH,
                       verify=False)
    return json.loads(res.content.decode('utf-8'))


def columns_to_str(columns):
    columns_str = ""
    for col in columns:
        columns_str += '&columns=' + col
    if columns_str:
        columns_str = '?' + columns_str[1:]
    return columns_str


def get_tools():
    res = requests.get(URL + 'asset?columns=ASSET_DATABASE_ID&columns=CURRENCY&columns=LABEL&columns=TYPE&columns=LAST_CLOSE_VALUE_IN_CURR&date=2012-01-01&CURRENCY=EUR',
                       auth=AUTH,
                       verify=False)
    return res.content.decode('utf-8')