#!/usr/bin/env python3
"""
contains TestAccessNestedMap class
"""

from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map
from unittest.mock import patch
from utils import memoize


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

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """method to test keyerror exception in access nested map"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """
    contains test for utils.getjson methods
    """
    def test_get_json(self):
        """
        method to use mocking of requests.get to test
        get_json method
        """
        pass


class TestMemoize(TestCase):
    """Tests the `memoize` function."""
    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
