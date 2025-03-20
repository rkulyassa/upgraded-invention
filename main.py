from typing import Union

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.middleware("http")
async def middleware(request: Request, call_next):
    user_id = request.query_params.get("user_id")
    if not user_id:
        user_id = request.client.host

    response = await call_next(request)
    return response
