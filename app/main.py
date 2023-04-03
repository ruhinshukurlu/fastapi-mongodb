from fastapi import FastAPI
from app.routers import post

app = FastAPI()

@app.get('/api/healthchecker')
def root():
    return {"message" : "Welcome to FastAPI with MongoDB"}


# app.include_router(post.router)
