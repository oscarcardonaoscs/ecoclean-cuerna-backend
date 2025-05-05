from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

# Crear cliente


@router.post("/", response_model=schemas.ClienteResponse)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.create_cliente(db=db, cliente=cliente)

# Obtener todos los clientes


@router.get("/", response_model=list[schemas.ClienteResponse])
def get_clientes(
    skip: int = 0,  # Paginación: Número de registros a omitir
    limit: int = 100,  # Paginación: Límite de registros a devolver
    search: str = "",  # Término de búsqueda
    db: Session = Depends(get_db),
):
    clientes = crud.get_clientes(db=db, skip=skip, limit=limit, search=search)
    return clientes

# Obtener un cliente por su ID


@router.get("/{cliente_id}", response_model=schemas.ClienteResponse)
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = crud.get_cliente(db=db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

# Actualizar cliente


@router.put("/{cliente_id}", response_model=schemas.ClienteResponse)
def update_cliente(cliente_id: int, cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = crud.update_cliente(
        db=db, cliente_id=cliente_id, cliente=cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

# Eliminar cliente


@router.delete("/{cliente_id}", response_model=schemas.ClienteResponse)
def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = crud.delete_cliente(db=db, cliente_id=cliente_id)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente
