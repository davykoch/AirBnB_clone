#!/usr/bin/python3
"""unittest for the class City"""

import unittest
import os
from models.city import City


class TestCity(unittest.TestCase):
    """unittest for the class City"""
    def test_attributes_initialization(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
