from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock: int


class CreateProduct(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True
