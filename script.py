import requests
from apscheduler.schedulers.background import BlockingScheduler
TRACK_API_URL = 'http://localhost:8080/track'


def track_request():
    print(f'Sending request to URL: [{TRACK_API_URL}]')
    requests.post(url=TRACK_API_URL)


scheduler = BlockingScheduler()
scheduler.add_job(track_request, 'interval', minutes=1)
scheduler.start()
