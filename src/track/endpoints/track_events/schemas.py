from datetime import datetime

from pydantic import BaseModel


class TrackEventCreate(BaseModel):
    request: str
    event_time: datetime
