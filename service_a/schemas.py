# Import BaseModel for validation
from pydantic import BaseModel


# Schema describing item data received from Service B
class Item(BaseModel):
    # ID of the item
    id: int

    # Name of the item
    name: str
