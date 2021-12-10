import json
from typing import List


def get_tmps_list() -> List[str]:
    # TODO: get template names from DB
    tmp_names: List[str] = ["взыскание заработной платы", "восстановление на рабочем месте"]
    return tmp_names


def get_regions_list() -> List[dict]:
    # TODO: get regions from DB
    with open("../../resources/regions.json") as f:
        regions: List[dict] = json.load(f)
        return regions


def get_region_code(region_name: str) -> str:
    # TODO: get regions from DB
    with open("../../resources/regions.json") as f:
        regions: List[dict] = json.load(f)
        code: int
        for regin in regions:
            if regin["name"] == region_name:
                return regin["code"]
        return -1
