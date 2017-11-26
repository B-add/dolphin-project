import json
from operator import itemgetter

from dataaccess.assets import get_tools
from dataaccess.ratios import compute_ratios


def get_best_sharpes_ids():
    asset_ids = [int(asset["ASSET_DATABASE_ID"]["value"]) for asset in
                 json.loads(get_tools())]
    sharpes = [(int(id), float(ratio["20"]["value"].replace(',', '.'))) for
               id, ratio in json.loads(
            compute_ratios(ratio_ids=[20], asset_ids=asset_ids)).items()]
    sharpes = (sorted(sharpes, key=itemgetter(1)))[-20:]
    return [item[0] for item in sharpes]