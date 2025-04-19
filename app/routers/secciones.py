from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

# Rutas CRUD para Secciones


# Eliminado el prefijo '/secciones'
@router.post("/", response_model=schemas.Seccion)
def create_seccion(seccion: schemas.SeccionCreate, db: Session = Depends(get_db)):
    return crud.create_seccion(db=db, seccion=seccion)


# Eliminado el prefijo '/secciones'
@router.get("/", response_model=list[schemas.Seccion])
def get_secciones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_secciones(db=db, skip=skip, limit=limit)


# Eliminado el prefijo '/secciones'
@router.get("/{seccion_id}", response_model=schemas.Seccion)
def get_seccion(seccion_id: int, db: Session = Depends(get_db)):
    db_seccion = crud.get_seccion(db=db, seccion_id=seccion_id)
    if db_seccion is None:
        raise HTTPException(status_code=404, detail="Sección no encontrada")
    return db_seccion


# Eliminado el prefijo '/secciones'
@router.put("/{seccion_id}", response_model=schemas.Seccion)
def update_seccion(seccion_id: int, seccion: schemas.SeccionCreate, db: Session = Depends(get_db)):
    db_seccion = crud.update_seccion(
        db=db, seccion_id=seccion_id, seccion=seccion)
    if db_seccion is None:
        raise HTTPException(status_code=404, detail="Sección no encontrada")
    return db_seccion


# Eliminado el prefijo '/secciones'
@router.delete("/{seccion_id}", response_model=schemas.Seccion)
def delete_seccion(seccion_id: int, db: Session = Depends(get_db)):
    db_seccion = crud.delete_seccion(db=db, seccion_id=seccion_id)
    if db_seccion is None:
        raise HTTPException(status_code=404, detail="Sección no encontrada")
    return db_seccion
