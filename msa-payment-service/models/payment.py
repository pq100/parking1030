from datetime import datetime
from sqlalchemy import Column, Integer, String, VARCHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Payment(Base):
    __tablename__ = 'payment'

    payid = Column(VARCHAR(30), primary_key=True, autoincrement=True, index=True)
    payment = Column(VARCHAR(50), nullable=False)
    paydate = Column(VARCHAR(30), nullable=False)
    carnum = Column(VARCHAR(50), ForeignKey=True , nullable=False)