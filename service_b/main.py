# FastAPI is the main framework
from fastapi import FastAPI

# List is used for type hinting (List[Item])
from typing import List

# Import Item schema (response structure)
from .schemas import Item


# Create FastAPI application instance
# This object represents the entire service
app = FastAPI(title="Service B - Items API")


# Define GET API endpoint at /items
# response_model ensures output matches List[Item]
@app.get("/items", response_model=List[Item])
async def get_items():
    """
    This function:
    - Handles incoming GET requests to /items
    - Returns a list of items
    - FastAPI automatically:
        - Validates output
        - Converts to JSON
        - Generates docs
    """

    # Returning hardcoded data for now
    # Later this will come from database
    return [
        Item(id=1, name="Apple"),
        Item(id=2, name="Banana"),
        Item(id=3, name="Orange"),
    ]
