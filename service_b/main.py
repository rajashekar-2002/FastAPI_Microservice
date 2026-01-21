from fastapi import FastAPI

app = FastAPI(title="Service B - Items API")

@app.get("/items")
async def get_items():
    return [
        {"id": 1, "name": "Apple"},
        {"id": 2, "name": "Banana"},
        {"id": 3, "name": "Orange"},
    ]
