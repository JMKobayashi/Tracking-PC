from datetime import datetime

from track.endpoints.base_use_case import BaseUseCase
from track.services.track_event_service import TrackEventService
from track.endpoints.track_events.schemas import TrackEventCreate


class TrackEventsUseCase(BaseUseCase):
    def __init__(self, track_event_service: TrackEventService) -> None:
        self._service = track_event_service

    async def run(self):
        track_event = TrackEventCreate(request='POST /track', event_time=datetime.now())
        return await self._service.create_track_event(track_event.dict())
