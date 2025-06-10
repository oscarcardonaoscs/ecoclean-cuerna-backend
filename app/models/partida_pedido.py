from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, Text
from sqlalchemy.orm import relationship
from app.database import Base


class PartidaPedido(Base):
    __tablename__ = "partidas_pedido"

    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False, default=1)
    precio_unitario = Column(DECIMAL(10, 4), nullable=False, default=0)
    importe = Column(DECIMAL(10, 4), nullable=False, default=0)
    notas = Column(Text, nullable=True)

    # Relaciones
    pedido = relationship("Pedido", back_populates="partidas")
    producto = relationship("Producto", lazy="joined")
