# app/routers/pagos.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from decimal import Decimal
from datetime import datetime

from app import schemas, models
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.PagoOut, status_code=status.HTTP_201_CREATED)
def crear_pago(
    pago_in: schemas.PagoCreate,
    db: Session = Depends(get_db),
):
    """
    Recibe un PagoCreate con:
      - pedido_id
      - forma_pago
      - monto_pagado
      - monto_recibido
      - monto_cambio
      - referencia_pago (opcional)
      - fecha_pago (opcional)

    Inserta un nuevo registro en la tabla `pagos`, luego recalcula
    el saldo y el estatus_pago del Pedido asociado, y devuelve el Pago creado.
    """

    # 1) Validar existencia del pedido
    pedido = db.query(models.Pedido).filter(
        models.Pedido.id == pago_in.pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")

    # 2) Crear el objeto Pago en la BD
    db_pago = models.Pago(
        pedido_id=pago_in.pedido_id,
        forma_pago=pago_in.forma_pago,
        monto_pagado=pago_in.monto_pagado,
        monto_recibido=pago_in.monto_recibido,
        monto_cambio=pago_in.monto_cambio,
        fecha_pago=pago_in.fecha_pago or datetime.utcnow(),
        referencia_pago=pago_in.referencia_pago,
    )
    db.add(db_pago)
    db.commit()
    db.refresh(db_pago)

    # 3) Recalcular el saldo y estatus_pago en Pedido
    total_pagado = (
        db.query(func.coalesce(func.sum(models.Pago.monto_pagado), 0))
        .filter(models.Pago.pedido_id == pago_in.pedido_id)
        .scalar()
    )
    # Nuevo saldo = total del pedido – suma de todos los pagos
    nuevo_saldo = pedido.total - Decimal(total_pagado)
    pedido.saldo = nuevo_saldo if nuevo_saldo > 0 else Decimal("0.00")

    # Determinar estatus_pago:
    if total_pagado >= pedido.total:
        pedido.estatus_pago = "Pagado"
    elif total_pagado > 0:
        pedido.estatus_pago = "Parcial"
    else:
        pedido.estatus_pago = "Pendiente"

    db.add(pedido)
    db.commit()
    db.refresh(pedido)

    return db_pago
