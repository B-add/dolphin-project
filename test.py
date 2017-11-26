import json
from operator import itemgetter

from dataaccess.assets import get_assets, get_asset, get_asset_attribute, \
    get_tools, get_asset_quotes
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
from funcs import get_covar, get_id_efficiency_volatility_tuple

print(get_id_efficiency_volatility_tuple())

# print(id_eff_vol)
# print(len(asset_ids))


