from decouple import config

SCREEN_WIDTH = config("SCREEN_WIDTH", default=800, cast=int)
SCREEN_HEIGHT = config("SCREEN_HEIGHT", default=530, cast=int)
APP_TITLE = config("APP_TITLE", default="Andromeda")
PLANETS_JSON_PATH = config("PLANETS_JSON_PATH", default="planets.json")
BLUETOOTH_NAME = config("BLUETOOTH_NAME", default="Andromeda")
SEND_COORD_MOCK_FILE = config("SEND_COORD_MOCK_FILE", default="/home/mock_coords.txt")
MIN_DEG_AZ = config("MIN_DEG_AZ", default=0.1, cast=float)
MIN_DEG_ALT = config("MIN_DEG_AZ", default=0.1, cast=float)
BLUETOOTH_MODE = config("BLUETOOTH_MODE", default="MOCK")
