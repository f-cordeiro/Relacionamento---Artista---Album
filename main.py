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

    albuns = relationship("Album", back_populates="artista")

    def __repr__(self):
        return f"Artista: {self.id}, nome: {self.nome}, genero:{self.genero}, país: {self.pais}, biografia: {self.biografia})"

class Album(Base):
    __tablename__ = "albuns"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    ano_lancamento = Column(Integer) 
    gravadora = Column(String(100))
    
    artista_id = Column(Integer, ForeignKey("artistas.id"))

    artista = relationship("Artista", back_populates="albuns")

    def __repr__(self):
        return f"Album: {self.id}, nome:{self.titulo}, ano:{self.ano_lancamento}, gravadora: {self.gravadora}, artista: {self.artista_id}"


engine = create_engine("sqlite:///produtora.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
