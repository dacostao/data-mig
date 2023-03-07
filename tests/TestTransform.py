import unittest
from app.etl.transform.Transform import Transform

class TestTransform(unittest.TestCase):

    def test_transform_hired_employees(self):
        input_data = [
            ['4535', 'Marcelo Gonzalez', '2021-07-27T16:02:08Z', '1', '2'],
            ['4572', 'Lidia Mendez', '2021-07-27T19:04:09Z', '1', '2']
        ]
        expected_data = [
            {'id': 4535, 'name': 'Marcelo Gonzalez', 'datetime': '2021-07-27T16:02:08Z', 'department_id': 1, 'job_id': 2},
            {'id': 4572, 'name': 'Lidia Mendez', 'datetime': '2021-07-27T19:04:09Z', 'department_id': 1, 'job_id': 2}
        ]
        actual_data = Transform.transform_hired_employees(input_data)
        self.assertEqual(actual_data,expected_data)

    def test_transform_departments(self):
        input_data = [
            ['1', 'Supply Chain'],
            ['2', 'Maintenance'],
            ['3', 'Staff']
        ]
        expected_data = [
            {'id': 1, 'department': 'Supply Chain'},
            {'id': 2, 'department': 'Maintenance'},
            {'id': 3, 'department': 'Staff'}
        ]
        actual_data = Transform.transform_departments(input_data)
        self.assertEqual(actual_data, expected_data)

    def test_transform_jobs(self):
        input_data = [
            ['1', 'Recruiter'],
            ['2', 'Manager'],
            ['3', 'Analyst']
        ]
        expected_data = [
            {'id': 1, 'job': 'Recruiter'},
            {'id': 2, 'job': 'Manager'},
            {'id': 3, 'job': 'Analyst'}
        ]
        actual_data = Transform.transform_jobs(input_data)
        self.assertEqual(actual_data, expected_data)
