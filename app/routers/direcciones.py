from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

# Crear dirección asociada a un cliente


@router.post("/clientes/{cliente_id}/direcciones/", response_model=schemas.DireccionResponse)
def create_direccion(cliente_id: int, direccion: schemas.DireccionCreate, db: Session = Depends(get_db)):
    return crud.create_direccion(db=db, direccion=direccion, cliente_id=cliente_id)

# Obtener todas las direcciones de un cliente


@router.get("/clientes/{cliente_id}/direcciones/", response_model=list[schemas.DireccionResponse])
def get_direcciones(cliente_id: int, db: Session = Depends(get_db)):
    return crud.get_direcciones(db=db, cliente_id=cliente_id)

# Obtener una dirección por su ID


@router.get("/{direccion_id}", response_model=schemas.DireccionResponse)
def get_direccion(direccion_id: int, db: Session = Depends(get_db)):
    db_direccion = crud.get_direccion(db=db, direccion_id=direccion_id)
    if db_direccion is None:
        raise HTTPException(status_code=404, detail="Dirección no encontrada")
    return db_direccion

# Actualizar una dirección


@router.put("/{direccion_id}", response_model=schemas.DireccionResponse)
def update_direccion(direccion_id: int, direccion: schemas.DireccionCreate, db: Session = Depends(get_db)):
    db_direccion = crud.update_direccion(
        db=db, direccion_id=direccion_id, direccion=direccion)
    if db_direccion is None:
        raise HTTPException(status_code=404, detail="Dirección no encontrada")
    return db_direccion

# Eliminar una dirección


@router.delete("/{direccion_id}", response_model=schemas.DireccionResponse)
def delete_direccion(direccion_id: int, db: Session = Depends(get_db)):
    db_direccion = crud.delete_direccion(db=db, direccion_id=direccion_id)
    if db_direccion is None:
        raise HTTPException(status_code=404, detail="Dirección no encontrada")
    return db_direccion
