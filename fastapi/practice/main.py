from enum import Enum
from fastapi import FastAPI, Query
from typing import Optional
# Optional은 편집기에서 오류를 찾을 수 있도록 도와주는 친구

app = FastAPI()

from routers import items, users
app.include_router(items.router)
app.include_router(users.router)

@app.get('/')
def root():
    return {'message' : 'ok'}

class modelEnum(str, Enum):
    model1 = 'red',
    model2 = 'blue',
    model3 = 'green'


@app.get('/route/{model_name}')
def model(model_name: modelEnum):
    if model_name == modelEnum.model1:
        return {
            'model': model_name,
            'message': 'model1'
        }
    elif model_name.value == "blue":
        return {
            'model': model_name,
            'message': 'model2'
        }
    return {
        'model': model_name,
        'message': 'model3'
    }

@app.get('/files/{file_path:path}')
def file(file_path: str):
    return {'file_path': file_path}

# url parameter 이용하기 (/params/?skip=10&take=30)
@app.get('/params/')
def params(skip: int = 0, take: int = 10):
    return {
        'skip': skip,
        'take': take
    }

