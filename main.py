from fastapi import FastAPI
from core.db import database
#from starlette.requests import Request
#from starlette.responses import Response
#from core.db import SessionLocal
from routes import routes
from core.fast_users import fastapi_users

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(routes)
app.include_router(fastapi_users.router, prefix="/users", tags=["users"])


# при запросе к нашим api(например blog.py) будет  Сессию для БД
# даже если api не нужна сессия все равно будет подниматся и сама закроется
# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     response = Response("Internal server error", status_code=500)
#     try:
#         request.state.db = SessionLocal()
#         response = await call_next(request)
#     finally:
#         request.state.db.close()  #сесия всегда будет закрыта
#     return response
