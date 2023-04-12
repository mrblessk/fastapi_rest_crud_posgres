from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import CardSchema, RequestCard, Response
import crud

# Init router
router = APIRouter()

# Init db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CRUD implementation
# Show all cards
@router.get('/')
async def get(db:Session=Depends(get_db)):
    _card = crud.get_card(db, 0, 100)
    return Response(code=200, status='Ok', message='Success Fetch all data', result=_card).dict(exclude_none=True)

# Show card by id
@router.get('/{id}')
async def get_by_id(id:str, db:Session=Depends(get_db)):
    _card = crud.get_card_by_id(db, card_id=id)
    return Response(code=200, status='Ok', message='Success get data', result=_card).dict(exclude_none=True)

# Create new card
@router.post('/create')
async def create(request:RequestCard, db:Session=Depends(get_db)):
    crud.create_card(db, card=request.parameter)
    return Response(code=200, status='Ok', message='Card created succesfully').dict(exclude_none=True)

# Update card info
@router.post('/update')
async def update_card(request:RequestCard, db:Session=Depends(get_db)):
    _attr = request.parameter
    _card = crud.update_card(db, card_id=_attr.id, name=_attr.name, cost=_attr.cost)
    return Response(code=200, status='Ok', message='Card updated succesfully', result=_card).dict(exclude_none=True)

# Delete card
@router.delete('/{id}')
async def delete(id:str, db:Session=Depends(get_db)):
    crud.remove_card(db, card_id=id)
    return Response(code=200, status='Ok', message='Card deleted succesfully').dict(exclude_none=True)
