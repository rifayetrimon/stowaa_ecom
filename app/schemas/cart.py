from pydantic import BaseModel


class CartItemBase(BaseModel):
    product_id: int
    quantity: int


class CreateCartItem(CartItemBase):
    pass


class CartItemResponse(CartItemBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
