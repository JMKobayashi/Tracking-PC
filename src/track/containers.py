from dependency_injector import containers, providers

from track.endpoints.track_events.use_cases.track_event import TrackEventsUseCase

from track.services.track_event_service import TrackEventService

from track.infrastructure.database.mongo import MongoDatabase
from track.repositories.track_event_repository import TrackEventRepository


class Container(containers.DeclarativeContainer):

    mongo_database = providers.Singleton(MongoDatabase, database='', host='', port='',
                                         user='', password='', authentication_source='',
                                         use_connection_string=True,
                                         connection_string='mongodb+srv://jamesmkobayashi:jamesmkobayashi@cluster0.8ljzolc.mongodb.net/?retryWrites=true&w=majority')
    track_event_mongo_repository = providers.Factory(TrackEventRepository,
                                                     session_factory=mongo_database.provided.session)
    track_event_service = providers.Factory(TrackEventService,
                                            mongo_repository=track_event_mongo_repository)
    track_events_use_case = providers.Factory(TrackEventsUseCase,
                                              track_event_service=track_event_service)
