from sqlalchemy import Column, Integer, String, Date, JSON
from sqlalchemy.dialects.postgresql import JSONB
from app.core.database import postgres_db

class BogieFormORM(postgres_db.Base):
    __tablename__ = "bogie_forms"

    id = Column(Integer, primary_key=True, index=True)
    formNumber = Column(String, unique=True, nullable=False)
    inspectionBy = Column(String, nullable=False)
    inspectionDate = Column(String, nullable=False)
    bogieDetails = Column(JSONB, nullable=False)
    bogieChecksheet = Column(JSONB, nullable=False)
    bmbcChecksheet = Column(JSONB, nullable=False)
    
    
class WheelSpecification(postgres_db.Base):
    __tablename__ = "wheel_specifications"

    id = Column(Integer, primary_key=True, index=True)
    form_number = Column(String, index=True)
    submitted_by = Column(String, index=True)
    submitted_date = Column(Date)

    condemning_dia = Column(String)
    last_shop_issue_size = Column(String)
    tread_diameter_new = Column(String)
    wheel_gauge = Column(String)
