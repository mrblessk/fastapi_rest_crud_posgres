from sqlalchemy.orm import Session
from model import Card
from schemas import CardSchema


# Show all cards
def get_card(db:Session, skip:int=0, limit:int=100):
    return db.query(Card).offset(skip).limit(limit).all()

# Show card by id
def get_card_by_id(db:Session, card_id:int):
    return db.query(Card).filter(Card.id == card_id).first()

# Create new card
def create_card(db:Session, card:CardSchema):
    _card = Card(name=card.name)
    db.add(_card)
    db.commit()
    db.refresh(_card)
    return _card

# Delete card
def remove_card(db:Session, card_id:int):
    _card = get_card_by_id(db=db, card_id=card_id)
    db.delete(_card)
    db.commit()

# Update card info
def update_card(db:Session, card_id:int, name:str, cost:int):
    _card = _card = get_card_by_id(db=db, card_id=card_id)
    _card.name = name
    _card.cost = cost
    db.commit()