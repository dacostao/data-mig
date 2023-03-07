import unittest
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

        query = self.session.query(Department).order_by(Department.id.desc())
        actual_data = [{'id': d.id, 'department': d.department} for d in query.all()]
        actual_data.reverse()   
        self.assertEqual(actual_data, data)

