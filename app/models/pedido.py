from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, DECIMAL, Text, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    folio = Column(String(20), unique=True, index=True, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    cliente = relationship("Cliente", back_populates="pedidos")
    fecha_creacion = Column(DateTime(timezone=True), default=datetime.utcnow)
    fecha_entrega = Column(DateTime, nullable=False)
    subtotal = Column(DECIMAL(10, 4), nullable=False, default=0)
    descuento = Column(DECIMAL(10, 4), nullable=False, default=0)
    envio = Column(DECIMAL(10, 4), nullable=False, default=0)
    iva = Column(DECIMAL(10, 4), nullable=False, default=0)
    total = Column(DECIMAL(10, 4), nullable=False, default=0)
    saldo = Column(Float, default=0.0)
    forma_pago = Column(String(50), nullable=False)
    estatus = Column(String(50), nullable=False, default="Pendiente")
    estatus_pago = Column(String(20), nullable=False, default="Pendiente")
    es_express = Column(Boolean, default=False)
    notas = Column(Text, nullable=True)
    fua = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relaciones
    partidas = relationship(
        "PartidaPedido", back_populates="pedido", cascade="all, delete-orphan")
    pagos = relationship("Pago", back_populates="pedido",
                         cascade="all, delete-orphan")
    historial_estatus = relationship(
        "PedidoStatusHistory",
        back_populates="pedido",
        order_by="PedidoStatusHistory.creado_en"
    )
