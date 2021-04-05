from sgp4.earth_gravity import wgs84
from sgp4.io import twoline2rv
from sgp4.ext import jday
from geocart import geo2cart, cart2geo
from spacetrack import SpaceTrackClient

import os
import getpass
import json
from datetime import datetime

satellites = []

"""
A TLE (two-line element set) is a two-line text containing information 
about the movement of an object in orbit around the Earth at a given time (noted “epoch”).
"""

def load_tle_data():
    """ Loads TLE data from tle.json and extrapolates orbit info """
    now = datetime.now()
    with open('tle.json', 'r') as f:
        data = json.load(f)
    
    for obj in data:
        tle_line1 = obj['TLE_LINE1']
        tle_line2 = obj['TLE_LINE2']
        debris = twoline2rv(tle_line1, tle_line2, wgs84)
        # The SGP4 propagator returns raw x,y,z Cartesian coordinates in a 
        # “True Equator Mean Equinox” (TEME) reference frame that’s centered 
        # on the Earth but does not rotate with it — an “Earth centered inertial” (ECI) 
        # reference frame
        position, velocity = debris.propagate(now.year, now.month, now.day, now.hour+1)
        d = {
            'satellite' : debris,
            'position'  : position,
            'velocity'  : velocity
        }
        satellites.append(d)

def get_current_location():
    pass

def find_nearby_debris(current_location: tuple):
    '''
    This function takes a tuple of x,y,z coordinates of current location,
    and return a list of nearby 'visible' debris
    '''
    pass

load_tle_data()
print(satellites[:10])