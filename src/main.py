import uvicorn
from fastapi import FastAPI

from web.get_requests import get_router
from web.post_requests import post_router


def get_application():
    app = FastAPI(title=__name__)

    app.include_router(router=get_router, prefix='/get')
    app.include_router(router=post_router, prefix='/post')

    return app


app = get_application()


if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8002)
