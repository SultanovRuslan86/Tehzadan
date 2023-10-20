from database import Base
from sqlalchemy import Column, Integer, String, DateTime

class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)

