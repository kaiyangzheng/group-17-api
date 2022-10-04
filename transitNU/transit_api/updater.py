from apscheduler.schedulers.background import BackgroundScheduler
from .train_update import update_train_info

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_train_info, 'interval', seconds=10)
    scheduler.start()