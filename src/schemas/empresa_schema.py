from pydantic import BaseModel


class EmpresaBase(BaseModel):
    nombre_empresa: str


class EmpresaCreate(EmpresaBase):
    pass


class EmpresaUpdate(EmpresaBase):
    pass


class EmpresaResponse(EmpresaBase):
    id_empresa: int

    class Config:
        from_attributes = True