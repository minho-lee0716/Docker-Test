from sqlalchemy import Column, Integer, String
from app.db.session import Base


class Song(Base):
    __tablename__ = "songs"
    __table_args__ = {
        "comment": "노래",
        "mysql_charset": "utf8mb4",
        "mysql_collate": "utf8mb4_general_ci"
    }

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    artist = Column(String(30), nullable=False, comment="가수 이름")
    title = Column(String(30), nullable=False, comment="노래 제목")
