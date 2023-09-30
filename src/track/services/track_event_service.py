import logging

from track.repositories.track_event_repository import TrackEventRepository
from track.endpoints.track_events.schemas import TrackEventCreate


class TrackEventService:
    def __init__(self, mongo_repository: TrackEventRepository) -> None:
        self._mongo_repository = mongo_repository

    async def create_track_event(self, params: TrackEventCreate):
        logging.info('Inserting track event to database')
        document = await self._mongo_repository.insert_one(params)
        logging.info('Track event inserted in database')

        return document
