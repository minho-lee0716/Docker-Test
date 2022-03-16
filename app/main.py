from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

from core.config import env_config, BASE_DIR
from router import router as playlist_router

from db.session import engine
from model import model

# Application
app = FastAPI(
    title="Docker Test",
    description="**Testing MySQL docker image & Dockerfile**",
    version="Beta",
    contact={
        "name": "이민호",
        "email": "minho.lee0716@gmail.com"
    },
)

# Cors
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=["*"],
)

# Model
# song.Base.metadata.create_all(bind=engine)

# Router
app.include_router(playlist_router.router)


if __name__ == "__main__":
    print('\n==================== Server Start ====================')
    print('ENV = ', env_config)
    print('BASE DIR = ', BASE_DIR, "\n")
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
