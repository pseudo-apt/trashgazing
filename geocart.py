"""
This module provides conversion between Geographic and Cartesian coordinates
"""

from math import cos, sin, asin, atan2, degrees, radians

R = 6371.137        # km, constant in wgs84 datum

def geo2cart(latitude, longitude):
    latitude = radians(latitude)
    longitude = radians(longitude)
    x = R * cos(latitude) * cos(longitude)
    y = R * cos(latitude) * sin(longitude)
    z = R * sin(latitude)

    return (x, y, z)

def cart2geo(x, y, z):
    latitude = degrees(asin(z / R))
    longitude = degrees(atan2(y, x))

    return (latitude, longitude)
