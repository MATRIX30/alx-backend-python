#!/usr/bin/env python3
"""
contains TestAccessNestedMap class
"""

from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """
    class to test functionalities of
    accessNestedMap
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Testing access nested map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
