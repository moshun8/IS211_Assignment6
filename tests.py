#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 6 Testing"""

from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit
from conversions import convertFahrenheitToCelsius, convertFahrenheitToKelvin
from conversions import convertKelvinToCelsius, convertKelvintoFahrenheit
import unittest


class TestC2K(unittest.TestCase):

    def setUp(self):
        self.temp1 = 300.00
        self.temp2 = 100.22
        self.temp3 = -100.00
        self.temp4 = -5000.10
        self.temp5 = 1234.56


    def test_simple(self):
        result1 = convertCelsiusToKelvin(self.temp1)
        self.assertEqual(result1, 573.15)


    def test_decimal(self):
        result2 = convertCelsiusToKelvin(self.temp2)
        self.assertEqual(result2, 373.37)


    def test_smallneg(self):
        result3 = convertCelsiusToKelvin(self.temp3)
        self.assertAlmostEqual(result3, 173.15)


    def test_largeneg(self):
        result4 = convertCelsiusToKelvin(self.temp4)
        self.assertAlmostEqual(result4, -4726.95)


    def test_largepos(self):
        result5 = convertCelsiusToKelvin(self.temp5)
        self.assertEqual(result5, 1507.71)


class TestC2F(unittest.TestCase):
    def setUp(self):
        self.temp1 = 300.00
        self.temp2 = 100.22
        self.temp3 = -100.00
        self.temp4 = -5000.10
        self.temp5 = 1234.56


    def test_simple(self):
        result1 = convertCelsiusToFahrenheit(self.temp1)
        self.assertEqual(result1, 572.00)


    def test_decimal(self):
        result2 = convertCelsiusToFahrenheit(self.temp2)
        self.assertAlmostEqual(result2, 212.396)


    def test_smallneg(self):
        result3 = convertCelsiusToFahrenheit(self.temp3)
        self.assertEqual(result3, -148.00)


    def test_largeneg(self):
        result4 = convertCelsiusToFahrenheit(self.temp4)
        self.assertEqual(result4, -8968.18)


    def test_largepos(self):
        result5 = convertCelsiusToFahrenheit(self.temp5)
        self.assertEqual(result5, 2254.208)


class TestF2C(unittest.TestCase):
    def setUp(self):
        self.temp1 = 300.00
        self.temp2 = 100.22
        self.temp3 = -100.00
        self.temp4 = -5000.10
        self.temp5 = 1234.56


    def test_simple(self):
        result1 = convertFahrenheitToCelsius(self.temp1)
        self.assertAlmostEqual(result1, 148.89, 2)


    def test_decimal(self):
        result2 = convertFahrenheitToCelsius(self.temp2)
        self.assertEqual(result2, 37.9)


    def test_smallneg(self):
        result3 = convertFahrenheitToCelsius(self.temp3)
        self.assertAlmostEqual(result3, -73.33, 2)


    def test_largeneg(self):
        result4 = convertFahrenheitToCelsius(self.temp4)
        self.assertAlmostEqual(result4, -2795.61, 2)


    def test_largepos(self):
        result5 = convertFahrenheitToCelsius(self.temp5)
        self.assertAlmostEqual(result5, 668.09, 2)


class TestF2K(unittest.TestCase):

    def setUp(self):
        self.temp1 = 300.00
        self.temp2 = 100.22
        self.temp3 = -100.00
        self.temp4 = -5000.10
        self.temp5 = 1234.56


    def test_simple(self):
        result1 = convertFahrenheitToKelvin(self.temp1)
        self.assertAlmostEqual(result1, 422.039, 3)


    def test_decimal(self):
        result2 = convertFahrenheitToKelvin(self.temp2)
        self.assertEqual(result2, 311.05)


    def test_smallneg(self):
        result3 = convertFahrenheitToKelvin(self.temp3)
        self.assertAlmostEqual(result3, 199.817, 3)


    def test_largeneg(self):
        result4 = convertFahrenheitToKelvin(self.temp4)
        self.assertAlmostEqual(result4, -2522.461, 3)


    def test_largepos(self):
        result5 = convertFahrenheitToKelvin(self.temp5)
        self.assertAlmostEqual(result5, 941.239, 3)


class TestK2C(unittest.TestCase):

    def setUp(self):
        self.temp1 = 300.00
        self.temp2 = 100.22
        self.temp3 = -100.00
        self.temp4 = -5000.10
        self.temp5 = 1234.56


    def test_simple(self):
        result1 = convertKelvinToCelsius(self.temp1)
        self.assertAlmostEqual(result1, 26.85, 2)


    def test_decimal(self):
        result2 = convertKelvinToCelsius(self.temp2)
        self.assertAlmostEqual(result2, -172.93, 2)


    def test_smallneg(self):
        result3 = convertKelvinToCelsius(self.temp3)
        self.assertEqual(result3, -373.15)


    def test_largeneg(self):
        result4 = convertKelvinToCelsius(self.temp4)
        self.assertEqual(result4, -5273.25)


    def test_largepos(self):
        result5 = convertKelvinToCelsius(self.temp5)
        self.assertEqual(result5, 961.41)


class TestK2F(unittest.TestCase):

    def setUp(self):
        self.temp1 = 300.00
        self.temp2 = 100.22
        self.temp3 = -100.00
        self.temp4 = -5000.10
        self.temp5 = 1234.56


    def test_simple(self):
        result1 = convertKelvintoFahrenheit(self.temp1)
        self.assertAlmostEqual(result1, 80.24, 2)


    def test_decimal(self):
        result2 = convertKelvintoFahrenheit(self.temp2)
        self.assertEqual(result2, -279.364)


    def test_smallneg(self):
        result3 = convertKelvintoFahrenheit(self.temp3)
        self.assertEqual(result3, -639.76)


    def test_largeneg(self):
        result4 = convertKelvintoFahrenheit(self.temp4)
        self.assertEqual(result4, -9459.94)


    def test_largepos(self):
        result5 = convertKelvintoFahrenheit(self.temp5)
        self.assertEqual(result5, 1762.448)


if __name__ == '__main__':
    unittest.main(exit=False)