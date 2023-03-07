import unittest
from app.etl.extract.ExtractCSV import ExtractCSV

class TestExtract(unittest.TestCase):

    def test_extract_csv_not_empty(self):
        filepath = 'data/hired_employees.csv'
        data = ExtractCSV.extract_file(filepath)
        self.assertIsNotNone(data)
