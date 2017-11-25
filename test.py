from dataaccess.assets import get_assets, get_asset, get_asset_attribute

from dataaccess.ratios import get_ratios, compute_ratios

# print(get_assets(full_response=False, columns=["MARKET_PLACE_CITY"]))

# print(get_assets(full_response=False, columns=["LABEL", "ASSET_DATABASE_ID"]))
#
#
# get_asset_attribute(220, 'LIQUIDITY_ALGO')

print(get_ratios())
print(compute_ratios(ratio_ids=[18], asset_ids=[220]))