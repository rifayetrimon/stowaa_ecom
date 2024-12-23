from pydantic import BaseModel
from typing import List


class OrderItemBase(BaseModel):
    product_id: int
    quantity: int
    price: float


class OrderBase(BaseModel):
    user_id: int
    total_amount: float
    status: str = "Pending"


class CreateOrder(OrderBase):
    items: List[OrderItemBase]


class OrderResponse(OrderBase):
    id: int
    items: List[OrderItemBase]

    class Config:
        orm_mode = True



# order item 


class OrderItemResponse(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    price: float

    class Config:
        orm_mode = True