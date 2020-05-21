from starlette.requests import Request

#ф-я получения стэйта
def get_db(request: Request):
    return request.state.db
