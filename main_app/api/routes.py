from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from .. import crud, schemas, scheduler
from ..database import get_db
from typing import List

router = APIRouter()

@router.get("/jobs", response_model=List[schemas.JobResponse])
def list_jobs(db: Session = Depends(get_db)):
    return crud.get_all_jobs(db)

@router.get("/jobs/{job_id}", response_model=schemas.JobResponse)
def get_job(job_id: str, db: Session = Depends(get_db)):
    job = crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/jobs", response_model=schemas.JobResponse)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    db_job = crud.create_job(db, job)
    scheduler.schedule_job(db_job.id, job.schedule)
    return db_job

@router.delete("/jobs/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(job_id: str, db: Session = Depends(get_db)):
    job = crud.get_job(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    scheduler.remove_job(job_id)
    crud.delete_job(db, job_id)
    return None
