from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.database import get_db

router = APIRouter()


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
