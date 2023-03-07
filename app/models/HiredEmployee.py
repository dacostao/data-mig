from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .DeclarativeBase import Base


class HiredEmployee(Base):
    __tablename__ = 'HiredEmployee'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    datetime = Column(DateTime, nullable=False)
    department_id = Column(Integer, ForeignKey('Department.id'), nullable=False)
    job_id = Column(Integer, ForeignKey('Job.id'), nullable=False)

    department = relationship('Department', backref='hired_employees', lazy=True)
    job = relationship('Job', backref='hired_employees', lazy=True)