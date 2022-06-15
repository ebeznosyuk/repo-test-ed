#!/usr/bin/env python3

import unittest
from main import count_sum, validate_realm

class MainTestCases(unittest.TestCase):

    def test_count_sum(self):
        # Given
        test_list = [5,5,5,6,6,6]

        # When
        result = count_sum(test_list)

        # Then
        expected_result = 33
        self.assertEquals(result, expected_result)

    def test_validate_realm(self):
        # Given
        realm = "AC"

        # When
        result = validate_realm(realm)

        # Then
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
