from datetime import datetime

from app.coordenates import get_planet_coord

def eq(val1, val2):
    return abs(val1 - val2) < 0.0001

def test_get_coord():

    base_date = datetime.fromisoformat('2012-12-12 10:10:10')
    lat = -19.5186257
    long = -40.6245297

    coord = get_planet_coord('moon', lat, long, base_date)

    az = float(coord.az.deg)
    alt = float(coord.alt.deg)

    assert eq(az, 98.9403819300) and eq(alt, 81.018271155)
