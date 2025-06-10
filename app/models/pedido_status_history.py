from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class PedidoStatusHistory(Base):
    __tablename__ = "pedido_status_history"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    estatus_anterior = Column(String(50), nullable=False)
    estatus_nuevo = Column(String(50), nullable=False)
    creado_en = Column(DateTime(timezone=True),
                       default=datetime.utcnow, nullable=False)

    pedido = relationship("Pedido", back_populates="historial_estatus")
