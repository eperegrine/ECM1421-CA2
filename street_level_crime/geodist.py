# geogdist.py
# Version 0.2

import math
from typing import Tuple

Coord = Tuple[float, float]

def distance( latlngA, latlngB):
    '''
    distance( (latA,lngA), (latB,lngB) ) -> float (distance in km)

    Returns the approximate straight line distance between two nearby points
    on the surface
    of the Earth assuming a sphere. With the default value of R of 6371.009
    the distance will be in kilometers.
    See also: https://en.wikipedia.org/wiki/Geographical_distance
    '''
    R = 6371.009 # approximate radius of earth surface (radius from center
                 # of the sphere in km)
    latA, lngA = latlngA
    lngA = math.radians(lngA)
    latA = math.radians(latA)
    latB, lngB = latlngB
    lngB = math.radians(lngB)
    latB = math.radians(latB)
    x = ( lngB - lngA ) * math.cos( (latA + latB) / 2 )
    y = latB - latA
    d = math.sqrt( x*x + y*y ) * R
    return d

def is_within_radius(latlngA: Coord, latlngB: Coord, radius: float) -> bool:
    """Checks if two cordinates are within a specified radius of eachother
    
    Arguments:
        latlngA {Tuple[int, int]} -- co-ordinate a
        latlngB {Tuple[int, int]} -- co-ordinate b
        radius {float} -- The radius to check
    
    Returns:
        bool -- whether or not the co-ordinates are within the specifed radius of eachother
    """    
    return distance(latlngA, latlngB) <= radius

if __name__ == "__main__":
    # Testing
    # TODO: Please verify the function by providing suitable test cases and
    # using asserts. The test should cover the cases your program is to deal
    # with, e.g. do not verify the correct distance between New York and London
    # For your testing allow a tolerance for the distance calculation as the
    # calculation is an approximation.

    uni_campus = (50.736544, -3.534948)
    #~= 1.6km google maps
    exeter_cathedral = (50.722548, -3.529915)
    dist = distance(uni_campus, exeter_cathedral)
    print(dist)
    assert abs(dist-1.6) < 0.01