#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6 Refactoring"""


class ConversionNotPossible(Exception): pass


def convert(fromUnit, toUnit, value=float):

    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    try:
        value = float(value)
    except TypeError:
        raise TypeError('Input should be a float ')

    # TIP FOUND ONLINE:
    # The easy way is to find a common base unit
    # and then just store the constant that is
    # used to convert from the base unit to that unit.
    # To convert from two units in the same category
    # (neither of which are the base unit), you simply
    # convert from your SOURCE_UNIT to the base unit, then
    # from that to the DESTINATION_UNIT.

    # Meters are the base unit 
    # tuple: (fromUnit to meter, meter to toUnit)
    convertLength = {
        'meters': (1.0, 1.0),
        'yards': (0.9144, 1.0936),
        'miles': (1609.344, 0.000621371192237)
    }

    # Celsius is the base unit 
    # tuple: (multiplication factor, addition value)
    convertTemps = {
        'celsius': (1.0, 0.0, 1.0),
        'fahrenheit': (1.8, 32.0, 0.55555),
        'kelvin': (1.0, 273.15, 1.0)
    }

    try:
        if fromUnit in convertLength and toUnit in convertLength:
            step1 = value * convertLength[fromUnit][0]
            step2 = step1 * convertLength[toUnit][1]
            return step2
        elif fromUnit in convertTemps and toUnit in convertTemps:
            step1 = (value - convertTemps[fromUnit][1]) * convertTemps[fromUnit][2]
            step2 = step1 * convertTemps[toUnit][0] + convertTemps[toUnit][1]
            return step2
    except:
        raise ConversionNotPossible("Can't convert length to/from temperature.")

