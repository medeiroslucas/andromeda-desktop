from datetime import datetime

import astropy.units as u
from astropy.coordinates import get_body, EarthLocation, AltAz
from astropy.time import Time


def get_planet_coord(planet: str, lat: float, long: float, date=None):

    utcoffset = -3*u.hour
    if not date:
        now = Time(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) - utcoffset
    else:
        now = date

    loc = EarthLocation(lat=lat, lon=long, height=0)

    plan = get_body(planet, time=now, location=loc)

    lf = AltAz(location=loc,
               obstime=now,
               pressure=1013.25*u.hPa,
               temperature=24*u.deg_C,
               relative_humidity=0.8)

    return plan.transform_to(lf)
