from track.endpoints.base_use_case import BaseUseCase
from track.services.get_track_events_service import GetTrackEventsService


class GetTrackEventsUseCase(BaseUseCase):
    def __init__(self, get_track_event_service: GetTrackEventsService) -> None:
        self._service = get_track_event_service

    async def run(self):
        print('Running track event retrieve')
        return await self._service.get_track_events()
