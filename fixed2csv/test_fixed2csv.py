from contextlib import contextmanager
from io import StringIO
import os
from textwrap import dedent
from tempfile import NamedTemporaryFile
import unittest

from fixed2csv import parse_fixed_width_file


class ParseFixedWidthFileTests(unittest.TestCase):

    """Tests for parse_fixed_width_file"""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_two_exact_columns(self):
        contents = dedent("""
            2012  Lexus
            2009  GMC
            1965  Ford
            2005  Hyundai
            1995  Mercedes-Benz
        """).lstrip()
        columns = [(0, 4), (6, 19)]
        expected = [
            ["2012", "Lexus"],
            ["2009", "GMC"],
            ["1965", "Ford"],
            ["2005", "Hyundai"],
            ["1995", "Mercedes-Benz"],
        ]
        self.assertIterableEqual(
            parse_fixed_width_file(StringIO(contents), columns),
            expected
        )

    def test_uneven_columns(self):
        contents = dedent("""
            2012  Lexus             LFA
            2009  GMC               Yukon XL 1500
            1965  Ford              Mustang
            2005  Hyundai           Sonata
            1995  Mercedes-Benz     C-Class
        """).lstrip()
        columns = [(0, 4), (6, 19), (24, 37)]
        expected = [
            ["2012", "Lexus", "LFA"],
            ["2009", "GMC", "Yukon XL 1500"],
            ["1965", "Ford", "Mustang"],
            ["2005", "Hyundai", "Sonata"],
            ["1995", "Mercedes-Benz", "C-Class"],
        ]
        self.assertIterableEqual(
            parse_fixed_width_file(StringIO(contents), columns),
            expected
        )

    def test_missing_data(self):
        contents = dedent("""
            2012  Lexus             LFA
                  Ford              Mustang
            2005  Hyundai           Sonata
            1995  Mercedes-Benz
        """).lstrip()
        columns = [(0, 4), (6, 19), (24, 31)]
        expected = [
            ["2012", "Lexus", "LFA"],
            ["", "Ford", "Mustang"],
            ["2005", "Hyundai", "Sonata"],
            ["1995", "Mercedes-Benz", ""],
        ]
        self.assertIterableEqual(
            parse_fixed_width_file(StringIO(contents), columns),
            expected
        )


# To test the Bonus part of this exercise, comment out the following line
# @unittest.expectedFailure
class ParseColumnsTests(unittest.TestCase):

    """Tests for parse_columns"""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_one_range(self):
        from fixed2csv import parse_columns
        self.assertIterableEqual(
            parse_columns('0:2'),
            [(0, 2)],
        )

    def test_two_ranges(self):
        from fixed2csv import parse_columns
        self.assertIterableEqual(
            parse_columns('0:4,6:19'),
            [(0, 4), (6, 19)],
        )

    def test_many_ranges(self):
        from fixed2csv import parse_columns
        self.assertIterableEqual(
            parse_columns('0:4,6:19,24:37'),
            [(0, 4), (6, 19), (24, 37)],
        )


# To test the Bonus part of this exercise, comment out the following line
@unittest.expectedFailure
class MainFunctionTests(unittest.TestCase):

    """Tests for main function"""

    def test_single_row(self):
        from fixed2csv import main
        contents = (
            "01  Otis Taylor                         "
            "Ran So Hard the Sun Went Down               "
            "3:52"
        )
        expected = '01,Otis Taylor,Ran So Hard the Sun Went Down,3:52\n'
        columns = '0:2,4:38,40:82,84:88'
        with make_file(contents) as fixed_file, make_file('') as csv_file:
            main([fixed_file, csv_file, '--cols=' + columns])
            self.assertEqual(open(csv_file).read(), expected)

    def test_multiple_rows_and_columns(self):
        from fixed2csv import main
        contents = dedent("""
            2012  Lexus             LFA
            2009  GMC               Yukon XL 1500
            1965  Ford              Mustang
            2005  Hyundai           Sonata
            1995  Mercedes-Benz     C-Class
        """).lstrip()
        expected = (
            "2012,Lexus,LFA\n"
            "2009,GMC,Yukon XL 1500\n"
            "1965,Ford,Mustang\n"
            "2005,Hyundai,Sonata\n"
            "1995,Mercedes-Benz,C-Class\n"
        )
        columns = '0:4,6:19,24:37'
        with make_file(contents) as fixed_file, make_file('') as csv_file:
            main(['--cols=' + columns, fixed_file, csv_file])
            self.assertEqual(open(csv_file).read(), expected)


@contextmanager
def make_file(contents=None):
    """Context manager providing name of a file containing given contents."""
    with NamedTemporaryFile(mode='wt', encoding='utf-8', delete=False) as f:
        if contents:
            f.write(contents)
    try:
        yield f.name
    finally:
        os.remove(f.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)