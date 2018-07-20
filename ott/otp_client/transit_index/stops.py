from ott.utils import object_utils
from ott.utils import geo_utils

from .base import Base

import logging
log = logging.getLogger(__file__)


class Stops(Base):
    """
    Scrolling map / BBOX call to stops:

    https://<domain & port>/otp/routers/default/index/stops?
      minLat=45.50854243338104&maxLat=45.519789433696744&minLon=-122.6960849761963&maxLon=-122.65591621398927
    [
        {
            id: TriMet:4026
            code: 4026
            name: SE Morrison & 9th
            lat: 45.517303
            lon: -122.656536
            url: http://trimet.org/#tracker/stop/4026
        }
    ]


    Nearest stops call:

    https://<domain & port>/otp/routers/default/index/stops?
    radius=1000&lat=45.4926336&lon=-122.63915519999999
    [
      {
        "id": "TriMet:5516",
        "code": "5516",
        "name": "SE Steele & 30th",
        "lat": 45.484781,
        "lon": -122.635074,
        "url": "http://trimet.org/#tracker/stop/5516",
        "dist": 928
      }
    ]
    """

    def __init__(self, args={}):
        super(Stops, self).__init__(args)
        object_utils.safe_set_from_dict(self, 'code', args)
        object_utils.safe_set_from_dict(self, 'name', args)
        object_utils.safe_set_from_dict(self, 'lat', args)
        object_utils.safe_set_from_dict(self, 'lon', args)
        object_utils.safe_set_from_dict(self, 'url', args)
        object_utils.safe_set_from_dict(self, 'mode', args, def_val="BUS")
        object_utils.safe_set_from_dict(self, 'dist', args, always_cpy=False)

    @classmethod
    def factory_via_svc(cls, bbox):
        # maybe call geoserver ????
        pass

    @classmethod
    def factory_via_db(cls, bbox):
        # call postgis within bbox
        pass

    @classmethod
    def factory_via_params(cls, min_lat, max_lat, min_lon, max_lon):
        bbox = geo_utils.bbox(min_lat, max_lat, min_lon, max_lon)
        stop = cls.factory_via_svc(bbox)
        return stop