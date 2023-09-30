import logging

from fastapi import APIRouter, Depends, HTTPException, FastAPI
from dependency_injector.wiring import inject, Provide
from track.endpoints.track_events.use_cases.track_event import TrackEventsUseCase
from track.endpoints.track_events.use_cases.get_track_events import GetTrackEventsUseCase

from track.containers import Container

router = APIRouter()


@router.post('/track')
@inject
async def create_track_event(request_event_use_case: TrackEventsUseCase =
                             Depends(Provide[Container.track_events_use_case])):
    try:
        logging.info('Received creation track event')
        return await request_event_use_case.run()
    except Exception as exception:
        logging.exception(exception.args)
        raise HTTPException(status_code=500, detail='Something went wrong')


@router.get('/track/events')
@inject
async def get_track_events(get_track_event_use_case: GetTrackEventsUseCase =
                           Depends(Provide[Container.get_track_events_use_case])):
    try:
        logging.info('Received retrieve track events')
        return await get_track_event_use_case.run()
    except Exception as exception:
        logging.exception(exception.args)
        raise HTTPException(status_code=500, detail='Something went wrong')


def configure(app: FastAPI):
    app.include_router(router=router)
