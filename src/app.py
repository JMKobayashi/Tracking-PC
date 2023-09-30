import uvicorn
from fastapi import FastAPI

from track.containers import Container


def create_app() -> FastAPI:
    app = FastAPI(openapi_url='/specs')

    container = Container()

    from track.endpoints.track_events import controllers as track_event
    track_event.configure(app=app)

    container.wire(modules=[track_event])

    app.container = container

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)
