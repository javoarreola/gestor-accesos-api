from pydantic import BaseModel

#DTOs de areas
class AreaBase(BaseModel):
    nombre_area: str


class AreaCreate(AreaBase):
    pass


class AreaUpdate(AreaBase): #similar a empresas, aqui la estructura sera llenada despues
    pass


class AreaResponse(AreaBase):
    id_area: int

    class Config:
        from_attributes = True