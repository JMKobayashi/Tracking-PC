from datetime import datetime
from odmantic import Model, Field


class TrackEventModel(Model):
    request: str = Field()
    event_time: datetime = Field()
