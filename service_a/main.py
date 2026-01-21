# FastAPI framework
from fastapi import FastAPI, Request

# Template engine to render HTML
from fastapi.templating import Jinja2Templates

# HTTP client for calling other services
import httpx

# Import schema for validation
from .schemas import Item


# Create FastAPI app instance
app = FastAPI(title="Service A - Frontend")

# Configure template directory
templates = Jinja2Templates(directory="service_a/templates")

# URL of Service B (hardcoded for now)
SERVICE_B_URL = "http://localhost:8001"


@app.get("/")
async def index(request: Request):
    """
    This function:
    - Handles browser request
    - Calls Service B
    - Renders HTML with data
    """

    # Create async HTTP client
    async with httpx.AsyncClient(timeout=2.0) as client:

        # Call Service B /items endpoint
        response = await client.get(f"{SERVICE_B_URL}/items")

        # Convert JSON response into Python dict
        raw_items = response.json()

        # Validate each item using Pydantic schema
        # This ensures data correctness
        items = [Item(**item) for item in raw_items]

    # Render HTML template
    return templates.TemplateResponse(
        "index.html",  # Template file
        {
            "request": request,  # REQUIRED for Jinja2
            "items": items       # Data passed to HTML
        }
    )
