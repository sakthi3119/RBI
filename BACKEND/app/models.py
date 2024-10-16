from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, index=True)
    account_holder = Column(String, index=True)
    contact_number = Column(String)
    account_number = Column(String, unique=True, index=True)
    current_location = Column(String)
    transaction_amount = Column(Float)
    transaction_history = Column(DateTime)
    is_mule = Column(Integer)  # 0 or 1
