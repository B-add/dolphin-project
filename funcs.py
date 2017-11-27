import json
from operator import itemgetter

import numpy as np
import math

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
             float(ratio["18"]["value"].replace(',', '.'))) for id, ratio in json.loads(compute_ratios(ratio_ids=[21, 18], asset_ids=assets_list, start_date='2012-01-01', end_date='2017-06-30')).items()]


def get_covar_mat(assets_list, e_v_assets_list):
    out = []
    min_ = 9999999999999

    for i in assets_list:
        out.append([quote["return"] for quote in get_asset_quotes(i, start_date='2012-01-01', end_date='2017-06-30')])
        if min_ > len(out[-1]):
            min_ = len(out[-1])

    for i in range(0, len(out)):
        out[i] = out[i][:min_]

    return np.cov(np.array(out)), np.mean(np.array(out), axis=1)


def optimize_assets(top=20, q=10):
    assets_list = get_best_sharpes_ids(top)
    e_v_assets_list = get_id_efficiency_volatility_tuple(assets_list)
    cov, means = get_covar_mat(assets_list, e_v_assets_list)

    print(cov)

    R = np.array([x[1] for x in e_v_assets_list])

    opt = optimize.approx_weight(cov, R, q, means, 0.01, 0.1)

    out = []

    for i in range(opt.shape[0]):
        out.append((assets_list[i], opt[i]))

    return out
