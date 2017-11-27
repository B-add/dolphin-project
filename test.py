import json
from operator import itemgetter

from dataaccess.assets import get_assets, get_asset, get_asset_attribute, \
    get_tools, get_asset_quotes

from funcs import get_best_sharpes_ids, get_covar_mat, optimize_assets

from dataaccess.portfolios import get_portfolio, get_our_portfolio, \
    set_test_portfolio

from dataaccess.ratios import get_ratios, compute_ratios

print(get_asset(id=443, full_response=False, columns=["LAST_CLOSE_VALUE"], date="2011-12-31"))

# print(get_asset(id=221, full_response=False, columns=["LABEL", "ASSET_DATABASE_ID"]))
# #
# #
# # get_asset_attribute(220, 'LIQUIDITY_ALGO')
#
# print(get_ratios())
# # print(compute_ratios(ratio_ids=[18], asset_ids=[220]))
#
# print(get_portfolio(221))

print(get_portfolio())

# print(get_portfolio())
from funcs import get_id_efficiency_volatility_tuple

# print(get_id_efficiency_volatility_tuple(get_best_sharpes_ids()))

# print(id_eff_vol)
# print(len(asset_ids))

# print(optimize_assets(2, 0))

set_test_portfolio([530, 446, 442, 389, 440, 505, 447, 419, 384, 466, 509, 478, 540, 370, 471, 393, 416, 441, 460, 443],
                   [0.530, 0.46, 0.442, 0.389, 0.440, 0.505, .447, .419, .384, .466, .509, .478, .540, .370, .471, .393, .416, .441, .460, .443])
print(optimize_assets(20, 100))
