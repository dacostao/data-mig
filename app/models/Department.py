from sqlalchemy import Column, String, Integer, ForeignKey
from .DeclarativeBase import Base

class Department(Base):
    __tablename__ = 'Department'
    
    id = Column(Integer, primary_key=True)
    department = Column(String(80), nullable=False)