from pydantic import BaseModel


class AreaBase(BaseModel):
    nombre_area: str


class AreaCreate(AreaBase):
    pass


class AreaUpdate(AreaBase):
    pass


class AreaResponse(AreaBase):
    id_area: int

    class Config:
        from_attributes = True