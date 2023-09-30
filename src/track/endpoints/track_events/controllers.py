from fastapi import APIRouter, Depends, HTTPException, FastAPI
from dependency_injector.wiring import inject, Provide
from track.endpoints.track_events.use_cases.track_event import TrackEventsUseCase

from track.containers import Container

router = APIRouter()


@router.post('/track')
@inject
async def create_track_events(request_event_use_case: TrackEventsUseCase = Depends(Provide[Container.track_events_use_case])):
    try:
        return await request_event_use_case.run()
    except Exception:
        raise HTTPException(status_code=500, detail='Something went wrong')


def configure(app: FastAPI):
    app.include_router(router=router)
