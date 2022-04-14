import unittest
import subprocess


class TestErrorHandling(unittest.TestCase):
    def test_wrong_join_type(self):
        self.assertNotEqual(0, subprocess.run(['join', 'a.csv', 'b.csv', 'color', 'some_join'],
                                              capture_output=True).returncode)

    def test_file_does_not_exist_first(self):
        self.assertNotEqual(0, subprocess.run(['join', 'does_not_exist.csv', 'b.csv', 'color'],
                                              capture_output=True).returncode)

    def test_file_does_not_exist_second(self):
        self.assertNotEqual(0, subprocess.run(['join', 'a.csv', 'does_not_exist.csv', 'color'],
                                              capture_output=True).returncode)

    def test_column_does_not_exist(self):
        self.assertNotEqual(0, subprocess.run(['join', 'a.csv', 'b.csv', 'not_column'],
                                              capture_output=True).returncode)


class TestInnerJoin(unittest.TestCase):
    def test_default_join(self):
        result = subprocess.run(['join', 'a.csv', 'b.csv', 'color'], capture_output=True)
        self.assertEqual(0, result.returncode)
        rows = set(result.stdout.decode('utf-8').strip().split())
        with open('ab_inner_join.csv') as answer:
            good_rows = set(answer.read().strip().split())
        self.assertEqual(good_rows, rows)

    def test_inner_join(self):
        result = subprocess.run(['join', 'a.csv', 'b.csv', 'color', 'inner'], capture_output=True)
        self.assertEqual(0, result.returncode)
        rows = set(result.stdout.decode('utf-8').strip().split())
        with open('ab_inner_join.csv') as answer:
            good_rows = set(answer.read().strip().split())
        self.assertEqual(good_rows, rows)


