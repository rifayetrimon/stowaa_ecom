# app/db/models/order.py
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)   
    status = Column(String, default="pending")
    total_price = Column(Float, nullable=False)

    user = relationship("User")
