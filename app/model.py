from sqlalchemy import Column, Integer, String
from config import Base


class Card(Base):
    """Base card model with essential attrs."""
    __tablename__ = 'card'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cost = Column(Integer)
