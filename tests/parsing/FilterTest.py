import unittest

from coalib import coala
from coalib.parsing.FilterHelper import FilterHelper, InvalidFilterException
from tests.TestUtilities import execute_coala, bear_test_module


class FilterTest(unittest.TestCase):

    def test_filter_by_language_c(self):
        with bear_test_module():
            retval, stdout, stderr = execute_coala(
                coala.main, 'coala', '-B', '--filter-by', 'language', 'c')
            self.assertEqual(retval, 0)
            # 1 bear plus 1 line holding the closing colour escape sequence.
            self.assertEqual(len(stdout.strip().splitlines()), 2)

    def test_filter_by_language_java_can_fix_syntax(self):
        with bear_test_module():
            retval, stdout, stderr = execute_coala(
                coala.main, 'coala', '-B',
                '--filter-by', 'language', 'java',
                '--filter-by', 'can_fix', 'syntax')
            self.assertEqual(retval, 0)
            # 1 line holding the closing colour escape sequence.
            self.assertEqual(len(stdout.strip().splitlines()), 1)
            self.assertIn('No bears to show.', stdout)

    def test_filter_by_language_java_can_detect_formatting(self):
        with bear_test_module():
            retval, stdout, stderr = execute_coala(
                coala.main, 'coala', '-B',
                '--filter-by', 'language', 'java',
                '--filter-by', 'can_detect', 'formatting')
            self.assertEqual(retval, 0)
            # 1 bear plus 1 line holding the closing colour escape sequence.
            self.assertEqual(len(stdout.strip().splitlines()), 2)

    def test_filter_bylanguage_java_can_detect_syntax(self):
        with bear_test_module():
            retval, stdout, stderr = execute_coala(
                coala.main, 'coala', '-B',
                '--filter-by-language', 'java',
                '--filter-by', 'can_detect', 'formatting')
            self.assertEqual(retval, 0)
            # 1 bear plus 1 line holding the closing colour escape sequence.
            self.assertEqual(len(stdout.strip().splitlines()), 2)

    def test_filter_by_can_detect_syntax(self):
        with bear_test_module():
            retval, stdout, stderr = execute_coala(
                coala.main, 'coala', '-B', '--filter-by',
                'can_detect', 'syntax')
            self.assertEqual(retval, 0)
            # 2 bears plus 1 line holding the closing colour escape sequence.
            self.assertEqual(len(stdout.strip().splitlines()), 3)

    def test_filter_by_can_detect_security(self):
        with bear_test_module():
            retval, stdout, stderr = execute_coala(
                coala.main, 'coala', '-B', '--filter-by',
                'can_detect', 'security')
            self.assertEqual(retval, 0)
            # 1 bear plus 1 line holding the closing colour escape sequence.
            self.assertEqual(len(stdout.strip().splitlines()), 2)

    def test_filter_by_can_detect_spelling(self):
        with bear_test_module():
            retval, stdout, stderr = execute_coala(
                coala.main, 'coala', '-B', '--filter-by',
                'can_detect', 'spelling')
            self.assertEqual(retval, 0)
            # 1 line holding the closing colour escape sequence.
            self.assertEqual(len(stdout.strip().splitlines()), 1)
            self.assertIn('No bears to show.', stdout)

    def test_filter_by_can_fix_syntax(self):
        with bear_test_module():
            retval, stdout, stderr = execute_coala(
                coala.main, 'coala', '-B', '--filter-by',
                'can_fix', 'syntax')
            self.assertEqual(retval, 0)
            # 1 line holding the closing colour escape sequence.
            self.assertEqual(len(stdout.strip().splitlines()), 1)
            self.assertIn('No bears to show.', stdout)

    def test_filter_by_can_fix_redundancy(self):
        with bear_test_module():
            retval, stdout, stderr = execute_coala(
                coala.main, 'coala', '-B', '--filter-by',
                'can_fix', 'redundancy')
            self.assertEqual(retval, 0)
            # 1 bear plus 1 line holding the closing colour escape sequence.
            self.assertEqual(len(stdout.strip().splitlines()), 2)

    def test_filter_by_unknown(self):
        with bear_test_module():
            retval, stdout, stderr = execute_coala(
                coala.main, 'coala', '-B', '--filter-by', 'unknown', 'arg1')
            self.assertEqual(retval, 2)
            self.assertRaisesRegex(InvalidFilterException,
                                   '{!r} is an invalid filter. Available '
                                   'filters: {}'.format(
                                       filter,
                                       FilterHelper.get_all_filters_str()))

    def test_filter_by_can_fix_null(self):
        with bear_test_module():
            retval, stdout, stderr = execute_coala(
                coala.main, 'coala', '-B', '--filter-by', 'can_fix')
            self.assertEqual(retval, 0)
            # 8 bears plus 1 line holding the closing colour escape sequence.
            self.assertEqual(len(stdout.strip().splitlines()), 14)

    def test_filter_by_can_detect_null(self):
        with bear_test_module():
            retval, stdout, stderr = execute_coala(
                coala.main, 'coala', '-B', '--filter-by', 'can_detect')
            self.assertEqual(retval, 0)
            # 8 bear plus 1 line holding the closing colour escape sequence.
            self.assertEqual(len(stdout.strip().splitlines()), 14)
