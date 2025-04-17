from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), index=True)  # Longitud de 200 caracteres
    precio = Column(Float)
    precioExpress = Column(Float)  # Agregado el campo de precio Express
    tipo = Column(String(5))  # Longitud de 5 caracteres para tipo
    # Campo booleano para indicar si está activo
    esActivo = Column(Boolean, default=True)
    # Campo de fecha y hora para FUA (Fecha de última actualización)
    fua = Column(DateTime, default=datetime.utcnow)

    # Clave foránea que apunta a Seccion
    seccion_id = Column(Integer, ForeignKey('secciones.id'))

    # Relación con Seccion
    seccion = relationship("Seccion", back_populates="productos")
