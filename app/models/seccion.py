from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship


class Seccion(Base):
    __tablename__ = 'secciones'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), index=True)

    # Relación con Producto
    productos = relationship("Producto", back_populates="seccion")
