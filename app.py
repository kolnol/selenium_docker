from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from Scrapper import Scrapper
import os
from datetime import datetime

def scrap_internal():
    router_url = os.getenv('ROUTER_URL')
    if router_url is None:
        raise AttributeError('ROUTER_URL is not set in an environment.')

    router_password = os.getenv('ROUTER_PASSWORD')
    if router_password is None:
        raise AttributeError('ROUTER_PASSWORD is not set in an environment.')
    
    print('=' * 10)
    scrapper = Scrapper(router_url, router_password)
    print('Running scraping ...')
    scrapper.run()
    print('=' * 10)

def scrap_schedule():
    now = datetime.now()
    print('Scheduled run for scrapping on: ', now)
    scrap_internal()

sched = BackgroundScheduler(daemon=True)
sched.add_job(scrap_schedule,'interval',weeks = 4)
sched.start()

app = Flask(__name__)

@app.route("/restart")
def restart_api():
    now = datetime.now()
    print('Restarting from api at: ', now)
    scrap_internal()
    return "Restarted"

if __name__ == "__main__":
    app.run()