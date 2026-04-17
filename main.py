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
        return f"nome: {self.nome}"

class Album(Base):
    __tablename__ = "albuns"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    ano_lancamento = Column(Integer) 
    gravadora = Column(String(100))
    

    artista_id = Column(Integer, ForeignKey("artistas.id"))


    artista = relationship("Artista", back_populates="albuns")

    def __repr__(self):
        return f"nome:{self.titulo}, ano:{self.ano_lancamento}"


engine = create_engine("sqlite:///produtora.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def cadastrar_artista():
    with Session() as session:
        try:
            nome_artista = input("Digite o nome do artista: ").capitalize().strip()
            genero = input("Digite o genero do artista:  ").capitalize().strip()
            pais = input("Digite o país do artista ").capitalize().strip()
            biografia = input("Digite a biografia do artista: ").capitalize()

            novo_artista = Artista(
                nome = nome_artista,
                genero = genero,
                pais = pais,
                biografia = biografia

            )

            session.add(novo_artista)
            session.commit()

            print(f"\n Artista {nome_artista} cadastrado com sucesso !!")
        except Exception as erro:
            session.rollback()
            print("Ocorreu um erro!")

# cadastrar_artista()

def cadastrar_album():
    with Session() as session:
        try:
            nome_album = input("Digite o nome do álbum: ").capitalize().strip()
            ano_lancamento = int(input("Digite o ano de lançamento do álbum: "))
            gravadora = input("Digite a gravadora do álbum: ").capitalize().strip()
            novo_artista = input("Digite o nome do artista:  ").capitalize().strip()

            artista_id = session.query(Artista).filter_by(nome=novo_artista).first()

            if artista_id is None:
                print("Artista não encontrado. Cadastre o novo artista primeiro!")
                return

            novo_album = Album(
                titulo = nome_album,
                ano_lancamento = ano_lancamento,
                gravadora = gravadora,
                artista = artista_id
            )

            session.add(novo_album)
            session.commit()

            print(f"\n Álbum {nome_album} cadastrado com sucesso !!")
        except Exception as erro:
            session.rollback()
            print("Ocorreu um erro!")

# cadastrar_album()

def listar_albuns():
    with Session() as session:
        try:
            todos_albuns = session.query(Album).all()

            if todos_albuns is None:
                print("Nenhum álbum cadastrado")
                return
            
            for album in todos_albuns:
                print(f"{album.titulo}")

        except Exception as erro:
            session.rollback()
            print("Ocorreu um erro!")

# listar_albuns()

def listar_albuns_artista():
    with Session() as session:
        try:
            nome = input("Digite o nome do artista: ").capitalize().strip()

            artista = session.query(Artista).filter_by(nome=nome).first()

            if artista is None:
                print(f"Artista {nome} não encontrado")
                return

            print(f"Álbuns de {nome} - {artista.albuns}")

        except Exception as erro:
            session.rollback()
            print("Ocorreu um erro!")  

# listar_albuns_artista() 

def listar_artistas_album():
    with Session() as session:
        try:
            artistas = session.query(Artista).all()
            
            for artista in artistas:
                if artista.albuns:
                    print(artista.nome)

        except Exception as erro:
            session.rollback()
            print("Ocorreu um erro!") 

# listar_artistas_album()

def atualizar_artista():
    with Session() as session:
        try:
            nome_busca = input("Digite o nome do artista: ").capitalize().strip()
            artista = session.query(Artista).filter_by(nome=nome_busca).first()

            if artista:
                print(f"Artista encontrado: {artista.nome}")

                novo_nome = input(f"Novo nome: ").strip()
                if novo_nome:
                    artista.nome = novo_nome.capitalize()
                
                novo_genero = input(f"Novo gênero {artista.genero}: ").strip()
                if novo_genero:
                    artista.genero = novo_genero.capitalize()

                novo_pais = input(f"Novo país {artista.pais}: ").strip()
                if novo_pais:
                    artista.pais = novo_pais.capitalize()

                novo_bio = input(f"Nova biografia {artista.biografia}: ").strip()
                if novo_bio:
                    artista.biografia = novo_bio.capitalize()
                
                session.commit()
                print("Dados atualizados com sucesso!")
            else:
                print("Artista não encontrado.")
                
        except Exception as erro:
            session.rollback()
            print(f"Erro ao atualizar: {erro}")

# atualizar_artista()