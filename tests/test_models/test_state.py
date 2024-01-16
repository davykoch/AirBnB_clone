#!/usr/bin/python3
"""unittest for the class State"""

import unittest
import os
from models.state import State


class TestState(unittest.TestCase):
    """unittest for class State"""
    def test_name_initialization(self):
        state = State()
        self.assertEqual(state.name, "")
