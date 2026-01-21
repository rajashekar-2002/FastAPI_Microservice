# Import BaseModel from Pydantic
# BaseModel is used to define data structure + validation rules
from pydantic import BaseModel


# This class defines how an Item should look in API responses
class Item(BaseModel):
    # id must be an integer
    id: int

    # name must be a string
    name: str

    class Config:
        # Allows converting ORM objects → Pydantic models
        # Very important when using SQLAlchemy later
        from_attributes = True
