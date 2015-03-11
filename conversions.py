#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6 Conversions"""


def convertCelsiusToKelvin(temp=float):
    try:
        x = temp + 273.15
    except TypeError:
        raise TypeError('Input should be a float ')
    return x


def convertCelsiusToFahrenheit(temp=float):
    try:
        x = temp * (9.0/5.0) + 32
    except TypeError:
        raise TypeError('Input should be a float')
    return x


def convertFahrenheitToCelsius(temp=float):
    try:
        x = (temp - 32) * (5.0/9.0)
    except TypeError:
        raise TypeError('Input should be a float')
    return x


def convertFahrenheitToKelvin(temp=float):
    try:
        x = (temp + 459.67) * (5.0/9.0)
    except TypeError:
        raise TypeError('Input should be a float')
    return x


def convertKelvinToCelsius(temp=float):
    try:
        x = temp - 273.15
    except TypeError:
        raise TypeError('Input should be a float')
    return x


def convertKelvintoFahrenheit(temp=float):
    try:
        x = temp * (9.0/5.0) - 459.76
    except TypeError:
        raise TypeError('Input should be a float')
    return x
