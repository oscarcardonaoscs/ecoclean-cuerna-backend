from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Direccion(Base):
    __tablename__ = 'direcciones'

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    calle = Column(String(255), nullable=True)
    numero_exterior = Column(String(50), nullable=True)
    numero_interior = Column(String(50), nullable=True)
    colonia = Column(String(100), nullable=True)
    municipio = Column(String(100), nullable=True)
    estado = Column(String(100), nullable=True)
    codigo_postal = Column(String(10), nullable=True)
    pais = Column(String(100), nullable=True)

    cliente = relationship("Cliente", back_populates="direcciones")
