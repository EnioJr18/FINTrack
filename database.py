from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from models import Base

DATABASE_URL = "sqlite:///.fintrack.db"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    print("Criando o banco de dados e as tabelas...")
    Base.metadata.create_all(bind=engine)
    print("Banco de dados e tabelas criados com sucesso!")