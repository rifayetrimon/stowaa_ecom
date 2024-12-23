from pydantic import BaseModel, Field


class ReviewBase(BaseModel):
    product_id: int
    user_id: int
    rating: int = Field(..., ge=1, le=5)  # Rating between 1 and 5
    comment: str | None = None


class CreateReview(ReviewBase):
    pass


class ReviewResponse(ReviewBase):
    id: int

    class Config:
        orm_mode = True
