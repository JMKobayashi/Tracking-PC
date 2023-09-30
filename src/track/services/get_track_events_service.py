from track.repositories.track_event_repository import TrackEventRepository


class GetTrackEventsService:
    def __init__(self, mongo_repository: TrackEventRepository) -> None:
        self._mongo_repository = mongo_repository

    async def get_track_events(self):
        print('Retrieving all track events')
        document = await self._mongo_repository.get_all()
        print('All track events retrieved')

        return document
