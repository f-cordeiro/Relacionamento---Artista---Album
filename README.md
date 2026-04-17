## SQLALCHEMY - Artista & Albuns

## By - Felipe Cordeiro e Gabriel Benedito

# Relacionamentos 1:N com SQLAlchemy

Este repositório contém um exemplo prático de como implementar e gerenciar relações **1:N (One-to-Many)** em Python, utilizando o **SQLAlchemy ORM**.

## O Conceito: 1 para N

No contexto de Artistas e Álbuns, o relacionamento **1:N** significa que:
* **1 Artista** pode estar relacionado a **Vários (N)** Álbuns.
* **1 Álbum** pertence a apenas **Um (1)** Artista.

Para que isso funcione no banco de dados, utilizamos uma **Foreign Key** (Chave Estrangeira) na "tabela filha" (Álbuns) apontando para a "tabela pai" (Artistas).

# Consultas e Persistência com SQLAlchemy

Este projeto demonstra como realizar operações de CRUD e consultas complexas utilizando o relacionamento entre as tabelas `artistas` e `albuns`.

## Funções de Consulta

O arquivo `main.py` utiliza a `Session` do SQLAlchemy para interagir com o banco de dados `produtora.db`. Abaixo estão os destaques das lógicas de consulta implementadas:

# Como Executar: 

## Pré-requisitos

Antes de executar o projeto, você precisa ter o Python instalado e instalar a biblioteca **SQLAlchemy**, que é o ORM utilizado para gerenciar o banco de dados SQLite.

### Instalação via Terminal

Execute o seguinte comando para instalar a dependência necessária:

```bash
pip install sqlalchemy
```

# Após instalar as dependências mencionadas acima, basta rodar o arquivo principal através do terminal:

```bash
python main.py