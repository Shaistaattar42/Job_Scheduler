from sqlalchemy.orm import Session
from .models import Job
from .schemas import JobCreate
from datetime import datetime
from uuid import uuid4

def get_all_jobs(db: Session):
    return db.query(Job).all()

def get_job(db: Session, job_id: str):
    return db.query(Job).filter(Job.id == job_id).first()

def create_job(db: Session, job: JobCreate):
    job_data = Job(
        id=str(uuid4()),
        name=job.name,
        schedule=job.schedule,
        created_at=datetime.utcnow()
    )
    db.add(job_data)
    db.commit()
    db.refresh(job_data)
    return job_data

def delete_job(db: Session, job_id: str):
    job = db.query(Job).filter(Job.id == job_id).first()
    if job:
        db.delete(job)
        db.commit()
