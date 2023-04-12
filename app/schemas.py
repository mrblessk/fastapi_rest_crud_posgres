from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

# Init dynamic type for use with generic
T = TypeVar('T')

class CardSchema(BaseModel):
    id: Optional[str] = None
    name: Optional[str] = None
    cost: Optional[int] = None

    class Config:
        orm_mode = True

class RequestCard(BaseModel):
    parameter: CardSchema = Field(...)


class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]