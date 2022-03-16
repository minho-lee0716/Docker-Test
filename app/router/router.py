from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.crud import (
    select_playlist,
    insert_playlist,
)
from app.db.session import db_conn
from app.schema.schema import (
    SongInput,
    SongList,
)

router = APIRouter(
    prefix="/playlist",
    tags=["PlayList"]
)


@router.get("", response_model=SongList)
async def my_playlist(db: Session = Depends(db_conn)):
    playlist = await select_playlist(db)
    return {"playlist": playlist}


@router.post("", response_model=SongList)
async def add_song_in_playlist(payload: SongInput, db: Session = Depends(db_conn)):
    playlist = await insert_playlist(payload, db)
    return {"playlist": playlist}
