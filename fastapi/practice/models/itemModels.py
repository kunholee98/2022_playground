from typing import List, Optional
from pydantic import BaseModel, HttpUrl, Field

class Image(BaseModel):
    url: HttpUrl = Field(..., example="http://example.com")
    name: str

class Item(BaseModel):
    name: str
    image: Optional[List[Image]] = None   # 하나의 모델을 다른 모델 내로 넣을 수 있다. (nested model)
    description: Optional[str] = None
    price: float
    tax: float=10.
    tags: List[str] = []

