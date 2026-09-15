from sqlalchemy import Column,Integer,String,Float,Boolean,DateTime
from database import Base
from datetime import datetime

class Job(Base):
    __tablename__="jobs"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(25))
    description=Column(String(250))
    location=Column(String(100))
    min_salary=Column(Float)
    max_Salary=Column(Float)
    is_active=Column(Boolean,default=True)
    created_At=Column(DateTime,default=datetime.now())

