from sqlalchemy.orm import Session

from app.model.model import Song
from app.schema.schema import SongInput


async def select_playlist(db: Session) -> list:
    return db.query(Song).order_by(Song.id.desc()).all()


async def insert_playlist(data: SongInput, db: Session):
    song = Song(**data.dict())
    db.add(song)
    db.commit()
    return db.query(Song).all()
