from pydantic import BaseModel
from typing import List


class SongInput(BaseModel):
    artist: str
    title: str


class SongDetail(SongInput):
    id: int

    class Config:
        orm_mode = True


class SongList(BaseModel):
    playlist: List[SongDetail]
