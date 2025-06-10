from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    razon_social = Column(String(100), nullable=True)
    rfc = Column(String(13), nullable=True)
    telefono = Column(String(15), nullable=True)
    email = Column(String(100), nullable=True)
    notas = Column(Text, nullable=True)
    tipo_pago = Column(String(50), nullable=True)
    es_habilitado = Column(Boolean, default=True)
    fua = Column(DateTime, default=datetime.utcnow)

    pedidos = relationship("Pedido", back_populates="cliente")
# Relación con direcciones
    direcciones = relationship(
        "Direccion", back_populates="cliente")
