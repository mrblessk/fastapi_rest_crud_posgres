from fastapi import FastAPI
import model
from config import engine
import router
import uvicorn

# Create tables in db
model.Base.metadata.create_all(bind=engine)

# Init Api
api = FastAPI()

@api.get('/')
async def Home():
    return "Welcome Home"

# Include urls from router.py
api.include_router(router.router, prefix='/card', tags=['card'])


if __name__ == '__main__':
    uvicorn.run(api, host='127.0.0.1', port=8000)