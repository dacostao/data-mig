from sqlalchemy import Column, String, Integer, ForeignKey
from .DeclarativeBase import Base

class Job(Base):
    __tablename__ = 'Job'
    
    id = Column(Integer, primary_key=True)
    job = Column(String(80), nullable=False)
