from pydantic import BaseModel


class EmpresaBase(BaseModel):
    nombre_empresa: str


class EmpresaCreate(EmpresaBase):
    pass


class EmpresaUpdate(EmpresaBase): #tanto update y create tienen un pass ya que estos espacios son rellenados por otras funciones, asi que solo se ocupa la estructura
    pass


class EmpresaResponse(EmpresaBase):
    id_empresa: int

    class Config:
        from_attributes = True