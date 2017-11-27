import json
from operator import itemgetter

import numpy as np

from dataaccess.assets import get_tools, get_asset_quotes
from dataaccess.ratios import compute_ratios
from optimize import optimize


def get_best_sharpes_ids(top=20):
    asset_ids = [int(asset["ASSET_DATABASE_ID"]["value"]) for asset in
                 json.loads(get_tools())]
    sharpes = [(int(id), float(ratio["20"]["value"].replace(',', '.'))) for
               id, ratio in json.loads(
            compute_ratios(ratio_ids=[20], asset_ids=asset_ids)).items()]
    sharpes = (sorted(sharpes, key=itemgetter(1)))[-top:]
    return [item[0] for item in sharpes]


def get_id_efficiency_volatility_tuple(assets_list):
    return [(int(id),
             float(ratio["21"]["value"].replace(',', '.')),
             float(ratio["18"]["value"].replace(',', '.'))) for id, ratio in json.loads(compute_ratios(ratio_ids=[21, 18], asset_ids=assets_list, start_date='2012-01-01', end_date='2017-06-01')).items()]


def get_covar(id_asset_1, id_asset_2):
    tmp_quotes_1 = [(quote["close"], quote["date"]) for quote in get_asset_quotes(id_asset_1, start_date='2012-01-01', end_date='2017-06-01')]
    tmp_quotes_2 = [(quote["close"], quote["date"]) for quote in get_asset_quotes(id_asset_2, start_date='2012-01-01', end_date='2017-06-01') if quote["date"] in [item[1] for item in tmp_quotes_1]]
    tmp_quotes_1 = [quote for quote in tmp_quotes_1 if quote[1] in [item[1] for item in tmp_quotes_2]]
    quotes_1 = np.array([item[0] for item in tmp_quotes_1])
    quotes_2 = np.array([item[0] for item in tmp_quotes_2])

    """
    print("===================")

    print(quotes_1[:10])
    print(np.mean(quotes_1[:10]))
    print(quotes_1[:10] - np.mean(quotes_1[:10]))

    print("==")

    print(quotes_2[:10])
    print(np.mean(quotes_2[:10]))
    print(quotes_2[:10] - np.mean(quotes_2[:10]))

    print("==")
    print((quotes_1[:10] - np.mean(quotes_1[:10])) * (quotes_2[:10] - np.mean(quotes_2[:10])))
    """

    return np.sum((quotes_1 - np.mean(quotes_1)) * (quotes_2 - np.mean(quotes_2))) / quotes_1.shape[0]


def get_covar_mat(assets_list, e_v_assets_list):
    out = np.ones((len(assets_list), len(assets_list)), dtype=float)

    for i in range(len(assets_list)):
        for j in range(i, len(assets_list)):
            if i == j:
                out[i, j] = e_v_assets_list[i][2]
            else:
                out[i, j] = get_covar(assets_list[i], assets_list[j])
                out[j, i] = out[i, j]

    return out

def optimize_assets(top=20, q=10):
    assets_list = get_best_sharpes_ids(top)
    e_v_assets_list = get_id_efficiency_volatility_tuple(assets_list)
    cov = get_covar_mat(assets_list, e_v_assets_list)

    print(cov)

    R = np.array([x[1] for x in e_v_assets_list])

    return optimize.approx_weight(cov, R, q, 0., 1.)
