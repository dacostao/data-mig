from app.models.DeclarativeBase import Base, engine, session
from app.models.Department import Department
from app.models.HiredEmployee import HiredEmployee
from app.models.Job import Job

class Load():

    Base.metadata.create_all(engine)

    def load_deparment(self, data):
        try:
            for row in data:
                department = Department(**row)
                session.add(department)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error occurred while loading data: {str(e)}")
        finally:
            session.close()

    def load_hired_employee(self, data):
        try:
            for row in data:
                hired_employee = HiredEmployee(**row)
                session.add(hired_employee)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error occurred while loading data: {str(e)}")
        finally:
            session.close()