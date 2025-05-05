from fastapi import APIRouter
from app.routers import pedidos

api_router = APIRouter()

# Incluyes el router aquí:
api_router.include_router(pedidos.router)
