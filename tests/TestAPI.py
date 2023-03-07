import unittest
import json
from sqlalchemy import inspect
from app.models.DeclarativeBase import engine, Session
from app.etl.load.Load import Load
from app.app import app


class APITestCase(unittest.TestCase):

    def setUp(self):
        self.load = Load()
        self.session = Session()
        self.client = app.test_client()
        self.client.testing = True

    def tearDown(self):
        self.session = Session()
        inspector = inspect(engine)

        for table_name in inspector.get_table_names():
            self.session.execute(f"DELETE FROM {table_name}")
            self.session.commit()

        self.session.close()

    def test_create_department(self):
        data = {
            'id': 1,
            'department': 'Supply Chain'
        }
        response = self.client.post('/api/department', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Department created successfully', response.data)

    def test_create_job(self):
        data = {
            'id': 1,
            'job': 'Recruiter'
        }
        response = self.client.post('/api/job', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Job created successfully', response.data)


    def test_create_employee(self):
        data = {
            'id': 4535,
            'name': 'Marcelo Gonzalez',
            'datetime': '2021-07-27T16:02:08Z',
            'department_id': 1,
            'job_id': 2
        }
        response = self.client.post('/api/hiredemployee', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Employee created successfully', response.data)
