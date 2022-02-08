from typing import List, Optional
from fastapi import APIRouter, Header, Query, Path, Body, UploadFile, File
# Query: 쿼리 파라미터들에 대한 validation
# Path: 패쓰 파라미터에 대한 validation

from tags import Tags

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

router = APIRouter(prefix="/items")

@router.get('/itemList',tags=[Tags.item])
def get_item_list(q: Optional[List[str]] = Query(None, title="Query string",
alias="item-query",
        description="Query string for the items to search in the database that have a good match",)):
    items = {'q':q}
    return items

# q : str = None -> 선택적으로 q를 가져가겠다는 의미

from models.itemModels import Item
from models.userModels import UserBase

@router.post('/postItem/',tags=[Tags.item])
async def postItem(
    authorization_1: Optional[str] = Header(None),
    item:Item = Body(...),
    user:UserBase = Body(..., example={"username":"kuno", "password": "1234", "description": "login"}), 
    importance: int = Body(...)
    ):
    print(authorization_1)
    return {
        'token': authorization_1,
        'user': user, 
        'item': item, 
        'importance': importance
    }   

@router.get('/{item_id}', response_model=Item, response_model_exclude_unset=False,tags=[Tags.item])
async def read_item(item_id: str):
    try:
        return items[item_id]
    except: 
        return {"id":1, "name": "", "price": 0}

@router.post('/files',tags=[Tags.item])
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@router.post('/uploadfile',tags=[Tags.item])
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}