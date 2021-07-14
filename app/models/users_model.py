from . import db

from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, Boolean

from sqlalchemy.orm import relationship, backref
from werkzeug.security import generate_password_hash, check_password_hash


class UsersModel(db.Model):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    is_admin = Column(Boolean, default=False)
    number = Column(String)

    credit_cards_lits = relationship("CreditCardsModel", backref="credit_cards")


    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

  
    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)