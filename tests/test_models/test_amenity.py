#!/usr/bin/python3
"""unittest for the class Amenity"""

import unittest
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """unittest for the class Amenity"""
    def test_name_initialization(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
