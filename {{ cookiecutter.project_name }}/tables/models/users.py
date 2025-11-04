from sqlalchemy import BigInteger, Column, Boolean

from tables.database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column("id", BigInteger, primary_key=True)
    is_admin = Column("is_admin", Boolean)