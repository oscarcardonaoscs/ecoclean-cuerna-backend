from fastapi import APIRouter, Depends, HTTPException, status
from decimal import Decimal
from sqlalchemy.orm import Session
from typing import List, Optional

from app.schemas.pedido import PedidoStatusUpdate, PedidoStatusHistoryOut
from app.models.pedido_status_history import PedidoStatusHistory
from app.crud.pedido import actualizar_estatus_pedido


from app import schemas, crud
from app.database import get_db

router = APIRouter()

# Endpoint para crear un pedido


@router.post("/", response_model=schemas.PedidoOut)
def crear_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    try:
        nuevo_pedido = crud.crear_pedido(db=db, pedido=pedido)
        return nuevo_pedido
    except Exception as e:
        print("ERROR AL GUARDAR PEDIDO:", e)
        raise HTTPException(
            status_code=400, detail=f"Error al crear el pedido: {str(e)}"
        )

# Endpoint para obtener todos los pedidos o filtrar por estatus


@router.get("/", response_model=List[schemas.PedidoOut])
def get_pedidos(
    db: Session = Depends(get_db),
    estatus: Optional[str] = None,
):
    if estatus:
        return crud.obtener_pedidos_por_estatus(db=db, estatus=estatus)
    return crud.obtener_todos_los_pedidos(db=db)


@router.put(
    "/{pedido_id}/cancelar",
    response_model=schemas.PedidoOut,
    status_code=status.HTTP_200_OK,
    summary="Cancelar un pedido"
)
def cancelar_pedido(
    pedido_id: int,
    db: Session = Depends(get_db)
):
    pedido = crud.obtener_pedido_por_id(db=db, pedido_id=pedido_id)
    if not pedido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pedido con id {pedido_id} no encontrado"
        )
    return crud.cancelar_pedido(db=db, pedido=pedido)


@router.patch(
    "/{pedido_id}/estatus",
    response_model=schemas.PedidoOut,
    status_code=status.HTTP_200_OK,
    summary="Actualizar estatus de un pedido"
)
def patch_estatus_pedido(
    pedido_id: int,
    body: PedidoStatusUpdate,
    db: Session = Depends(get_db)
):
    pedido = crud.obtener_pedido_por_id(db=db, pedido_id=pedido_id)
    if not pedido:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pedido con id {pedido_id} no encontrado"
        )
    actualizado = actualizar_estatus_pedido(
        db=db, pedido_id=pedido_id, nuevo_estatus=body.estatus
    )
    return actualizado


@router.get("/{pedido_id}/historial", response_model=List[PedidoStatusHistoryOut])
def get_historial(
    pedido_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(PedidoStatusHistory)
        .filter(PedidoStatusHistory.pedido_id == pedido_id)
        .order_by(PedidoStatusHistory.creado_en)
        .all()
    )
