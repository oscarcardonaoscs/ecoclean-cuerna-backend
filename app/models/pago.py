from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime


class Pago(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    forma_pago = Column(String(50), nullable=False)

    monto_pagado = Column(DECIMAL(10, 4), nullable=False, default=0)
    monto_recibido = Column(DECIMAL(10, 4), nullable=False, default=0)
    monto_cambio = Column(DECIMAL(10, 4), nullable=False, default=0)

    fecha_pago = Column(DateTime, default=datetime.utcnow)
    referencia_pago = Column(String(255), nullable=True)

    # Relaciones
    pedido = relationship("Pedido", back_populates="pagos")
