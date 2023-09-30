import requests
from apscheduler.schedulers.background import BlockingScheduler
TRACK_API_URL = 'https://track-challenge-ucu2fzh5qa-uc.a.run.app/track'


def track_request():
    print(f'Sending request to URL: [{TRACK_API_URL}]')
    requests.post(url=TRACK_API_URL)


scheduler = BlockingScheduler()
scheduler.add_job(track_request, 'interval', minutes=1)
scheduler.start()
