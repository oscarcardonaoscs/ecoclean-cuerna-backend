from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir Base para la creación de modelos
Base = declarative_base()

# Configuración de la base de datos (con MySQL y pymysql)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:nebrac2Ucj$@localhost/ecoclean"

# Crear el motor de la base de datos sin 'check_same_thread'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Crear la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para obtener la sesión de la base de datos


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
