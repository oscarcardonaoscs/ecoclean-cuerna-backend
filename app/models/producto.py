from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship


class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), index=True)
    precio = Column(Float)

    # Clave foránea que apunta a Seccion
    seccion_id = Column(Integer, ForeignKey('secciones.id'))

    # Relación con Seccion
    seccion = relationship("Seccion", back_populates="productos")
