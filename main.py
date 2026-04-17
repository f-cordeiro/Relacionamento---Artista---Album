from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Artista(Base):
    __tablename__ = "artistas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    genero = Column(String(50))
    pais = Column(String(50))
    biografia = Column(Text)

    def __repr__(self):
        return f"Artista: {self.id}, nome: {self.nome}, genero:{self.genero}, país: {self.pais}, biografia: {self.biografia})"