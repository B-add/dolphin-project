import json
from operator import itemgetter

from dataaccess.assets import get_assets, get_asset, get_asset_attribute, \
    get_tools
from dataaccess.portfolios import get_portfolio, get_our_portfolio

from dataaccess.ratios import get_ratios, compute_ratios

# print(get_assets(full_response=False, columns=["MARKET_PLACE_CITY"]))

# print(get_asset(id=221, full_response=False, columns=["LABEL", "ASSET_DATABASE_ID"]))
# #
# #
# # get_asset_attribute(220, 'LIQUIDITY_ALGO')
#
# print(get_ratios())
# # print(compute_ratios(ratio_ids=[18], asset_ids=[220]))
#
# print(get_portfolio(221))

# print(get_portfolio())


# id_eff_vol_2012_2017 = [(int(id),
#                  float(ratio["21"]["value"].replace(',', '.')),
#                  float(ratio["18"]["value"].replace(',', '.'))) for id, ratio in json.loads(compute_ratios(ratio_ids=[21, 18], asset_ids=asset_ids, start_date='2012-01-01', end_date='2017-06-01')).items()]


# print(id_eff_vol)
# print(len(asset_ids))


