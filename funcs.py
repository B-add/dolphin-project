import json
from operator import itemgetter

import numpy as np

from dataaccess.assets import get_tools, get_asset_quotes
from dataaccess.ratios import compute_ratios


def get_best_sharpes_ids():
    asset_ids = [int(asset["ASSET_DATABASE_ID"]["value"]) for asset in
                 json.loads(get_tools())]
    sharpes = [(int(id), float(ratio["20"]["value"].replace(',', '.'))) for
               id, ratio in json.loads(
            compute_ratios(ratio_ids=[20], asset_ids=asset_ids)).items()]
    sharpes = (sorted(sharpes, key=itemgetter(1)))[-20:]
    return [item[0] for item in sharpes]


def get_covar(id_asset_1, id_asset_2):
    quotes_1 = np.array([quote["close"] for quote in get_asset_quotes(id_asset_1, start_date='2012-01-01', end_date='2017-06-01')])
    quotes_2 = np.array([quote["close"] for quote in get_asset_quotes(id_asset_2, start_date='2012-01-01', end_date='2017-06-01')])
    return np.sum((quotes_1 - np.mean(quotes_1)) * (quotes_2 - np.mean(quotes_2))) / quotes_1.shape[0]
