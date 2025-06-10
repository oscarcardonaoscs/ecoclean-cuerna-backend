from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class PagoBase(BaseModel):
    forma_pago: str
    monto_pagado: float
    monto_recibido: float
    monto_cambio: float
    referencia_pago: Optional[str] = None


class PagoCreate(PagoBase):
    pedido_id: int
    fecha_pago: Optional[datetime] = None

    class Config:
        orm_mode = True


class PagoOut(PagoBase):
    id: int
    pedido_id: int
    fecha_pago: datetime

    class Config:
        orm_mode = True
