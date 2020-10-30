from sgp4.earth_gravity import wgs84
from sgp4.io import twoline2rv
from sgp4.ext import jday
from geocart import geo2cart, cart2geo

import os
import getpass
from datetime import datetime

satellites = []

def download_tle():
    pass

def load_tle_data():
    now = datetime.now()
    with open('tle.txt', 'r') as f:
        while True:
            try:
                line1 = f.readline()
                line2 = f.readline()
                debris = twoline2rv(line1, line2, wgs84)
                position, velocity = debris.propagate(
                    now.year, now.month, now.day, now.hour+1)
                d = {
                    'satellite' : debris,
                    'position'  : position,
                    'velocity'  : velocity
                }
                satellites.append(d)
            except:
                return

def get_current_location():
    pass

def find_nearby_debris(current_location: tuple):
    '''
    This function takes a tuple of x,y,z coordinates of current location,
    and return a list of nearby 'visible' debris
    '''

#download_tle()
#load_tle_data()
#print(satellites)
#print(len(satellites))
