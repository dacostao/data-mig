import unittest
import datetime
from sqlalchemy import inspect
from app.models.DeclarativeBase import engine, Session
from app.models.Department import Department
from app.models.HiredEmployee import HiredEmployee
from app.models.Job import Job
from app.etl.load.Load import Load

class TestLoad(unittest.TestCase):

    def setUp(self):
        self.load = Load()
        self.session = Session()

    def tearDown(self):
        self.session = Session()
        inspector = inspect(engine)

        for table_name in inspector.get_table_names():
            self.session.execute(f"DELETE FROM {table_name}")
            self.session.commit()

        self.session.close()

    def test_load_department_data(self):
        data = [
            {'id': 1, 'department': 'Supply Chain'},
            {'id': 2, 'department': 'Maintenance'},
            {'id': 3, 'department': 'Staff'}
        ]

        self.load.load_deparment(data)

        query = self.session.query(Department).order_by(Department.id.asc())
        actual_data = [{'id': d.id, 'department': d.department} for d in query.all()]
        self.assertEqual(actual_data, data)

    def test_load_hired_employee_data(self):
        data = [
            {'id': 4535,'name': 'Marcelo Gonzalez', 'datetime': datetime.datetime(2021, 7, 27, 16, 2, 8), 'department_id': 1, 'job_id': 2},
            {'id': 4572,'name': 'Lidia Mendez', 'datetime': datetime.datetime(2021, 7, 27, 19, 4, 9), 'department_id': 1, 'job_id': 2}
        ]

        self.load.load_hired_employee(data)

        query = self.session.query(HiredEmployee).order_by(HiredEmployee.id.asc())
        actual_data = [{'id': h.id, 
                        'name': h.name, 
                        'datetime': h.datetime, 
                        'department_id':h.department_id, 
                        'job_id': h.job_id} 
                        for h in query.all()]
        
        data = sorted(data, key=lambda h: h['id'])
        actual_data = sorted(actual_data, key=lambda h: h['id'])
        self.assertEqual(actual_data, data)

    def test_load_job_data(self):
        data = [
            {'id': 1, 'job': 'Recruiter'},
            {'id': 2, 'job': 'Manager'},
            {'id': 3, 'job': 'Analyst'}
        ]

        self.load.load_job(data)

        query = self.session.query(Job).order_by(Job.id.asc())
        actual_data = [{'id': j.id, 'job': j.job} for j in query.all()]
        self.assertEqual(actual_data, data)