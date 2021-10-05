from decouple import config

SCREEN_WIDTH = config("SCREEN_WIDTH", default=800, cast=int)
SCREEN_HEIGHT = config("SCREEN_HEIGHT", default=530, cast=int)
APP_TITLE = config("APP_TITLE", default="Andromeda")
PLANETS_JSON_PATH = config("PLANETS_JSON_PATH", default="planets.json")
