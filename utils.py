import json
from setting import PLANETS_JSON_PATH


def get_planets_dict(planets_json_path=PLANETS_JSON_PATH):

    with open(planets_json_path,) as fil:
        plantes_json = json.load(fil)

    return plantes_json
