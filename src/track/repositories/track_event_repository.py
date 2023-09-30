from track.infrastructure.repositories.mongo_repository import MongoRepository
from track.model.track_event_model import TrackEventModel


class TrackEventRepository(MongoRepository):
    model = TrackEventModel
