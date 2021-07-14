from . import db

from sqlalchemy import Column, Integer, String, ForeignKey


class CreditCardsModel(db.Model):

    __tablename__ = "credit_cards"

    id = Column(Integer, primary_key=True)

    expire_date = Column(String(30), nullable=False)
    number = Column(String(30), nullable=False, unique=True)
    provider = Column(String(50), nullable=False)
    security_code = Column(String(3))
    
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    