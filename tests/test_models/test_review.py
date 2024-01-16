#!/usr/bin/python3
"""unittest for the class Review"""

import unittest
import os
from models.review import Review


class TestReview(unittest.TestCase):
    """unittest for the class Review"""
    def test_attributes_initialization(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
