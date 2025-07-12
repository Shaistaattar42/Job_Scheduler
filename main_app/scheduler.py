from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .jobs import dummy_job

scheduler = BackgroundScheduler()

def schedule_job(job_id: str, day_of_week: str):
    scheduler.add_job(
        func=dummy_job,
        trigger=CronTrigger(day_of_week=day_of_week, hour=10, minute=0),
        id=job_id,
        replace_existing=True
    )

def remove_job(job_id: str):
    try:
        scheduler.remove_job(job_id)
    except Exception as e:
        print(f"Error removing job: {e}")
        

def start_scheduler():
    scheduler.start()