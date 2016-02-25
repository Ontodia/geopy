
from __future__ import print_function
import sys
import unittest

from geopy.compat import u
from geopy.geocoders import Geoclient
from test.geocoders.util import GeocoderTestBase, env

class GeoclientTestCaseUnitTest(GeocoderTestBase):  # pylint: disable=R0904,C0111

    def test_user_agent_custom(self):
        geocoder = Geoclient(
            app_id='DUMMY12345',
            app_key='DUMMY67890',
            user_agent='my_user_agent/1.0'
        )
        self.assertEqual(geocoder.headers['User-Agent'], 'my_user_agent/1.0')


@unittest.skipUnless(  # pylint: disable=R0904,C0111
    bool(env.get('GEOCLIENT_APP_KEY')) and \
    bool(env.get('GEOCLIENT_APP_ID')),
    "No GEOCLIENT_APP_KEY and GEOCLIENT_APP_ID env variables set"
)
class GeoclientTestCase(GeocoderTestBase): # pylint: disable=R0904,C0111

    @classmethod
    def setUpClass(cls):
        app_id=env['GEOCLIENT_APP_ID']
        app_key=env['GEOCLIENT_APP_KEY']
        print("app_id: ", app_id, file=sys.stderr)
        print("app_key: ", app_key, file=sys.stderr)
        cls.geocoder = Geoclient(app_id, app_key)
        cls.delta = 0.04

    def test_geocode_address(self):
        """
        Geoclient.geocode
        """
        self.geocode_run(
            {"query": "85 Fifth Ave, Manhattan, NY"},
            {"latitude": 40.73727812604426, "longitude": -73.99215518677124}
        )

    def test_geocode_bin(self):
        """
        Geoclient.geocode Building ID Number
        """
        self.geocode_run(
            {"query": "1079043"},
            {"latitude": 40.7086585249236, "longitude": -74.00798211500157}
        )
        
    def test_geocode_intersection(self):
        """
        Geoclient.geocode Intersection
        """
        self.geocode_run(
            {"query": "Broadway and W 100 St"},
            {"latitude": 40.797216857686585, "longitude": -73.96991438209491}
        )

