from unittest import TestCase


class TestFib_iterative(TestCase):
    def test_fib_iterative(self):
        try:
            from build import fib_iterative
        except ImportError:
            self.assertFalse("no function found")
        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(expected)):
            result.append(fib_iterative(i))
        self.assertEqual(result, expected)

    def test_fib_recursive(self):
        try:
            from build import fib_recursive
        except ImportError:
            self.assertFalse("no function found")
        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(expected)):
            result.append(fib_recursive(i))
        self.assertEqual(result, expected)

    def test_fib_dynamic(self):
        try:
            from build import fib_dynamic
        except ImportError:
            self.assertFalse("no function found")
        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(expected)):
            result.append(fib_dynamic(i))
        self.assertEqual(result, expected)
