from sqlalchemy import Column, Integer, String, Numeric, Date


from src.database.models import Base


class Currency(Base):
    __tablename__ = "currencies"
    code = Column(String(10), primary_key=True)
    num_code = Column(Integer)
    char_code = Column(String(15))
    name = Column(String)
    nominal = Column(Integer)
    value = Column(Numeric(10, 4))
    date_req = Column(Date, primary_key=True)
