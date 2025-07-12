from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.mysql import VARCHAR
from datetime import datetime
from uuid import uuid4
from .database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(VARCHAR(36), primary_key=True, default=lambda: str(uuid4()))
    name = Column(String(255), nullable=False)
    schedule = Column(String(255), nullable=False)
    last_run = Column(DateTime, nullable=True)
    next_run = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)