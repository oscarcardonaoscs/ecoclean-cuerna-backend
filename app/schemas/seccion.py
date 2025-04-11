from pydantic import BaseModel
from typing import Optional


class SeccionBase(BaseModel):
    nombre: str

    class Config:
        orm_mode = True


class SeccionCreate(SeccionBase):
    pass


class SeccionUpdate(SeccionBase):
    pass


class Seccion(SeccionBase):
    id: int

    class Config:
        orm_mode = True
