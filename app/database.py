from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir Base para la creación de modelos
Base = declarative_base()

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:nebrac2Ucj$@localhost/ecoclean"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
