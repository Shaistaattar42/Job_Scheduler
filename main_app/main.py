from fastapi import FastAPI
from main_app.database import Base, engine
from main_app.api.routes import router as job_router
from main_app import scheduler

app = FastAPI(title="Job Scheduler Microservice")

Base.metadata.create_all(bind=engine)
scheduler.start_scheduler()

app.include_router(job_router)

@app.get("/")
def root():
    return {"message": "Job Scheduler is running"}