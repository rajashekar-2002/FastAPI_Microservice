# 🔁 How services interact (VERY IMPORTANT)
# Step-by-step flow

# 1️⃣ Browser requests / from Service A
# 2️⃣ Service A calls /items on Service B
# 3️⃣ Service B returns JSON
# 4️⃣ Service A renders HTML
# 5️⃣ Browser sees result

# 📌 Service B never talks to HTML
# 📌 Service A never owns data



from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import httpx

app = FastAPI(title="Service A - Frontend")

templates = Jinja2Templates(directory="service_a/templates")

SERVICE_B_URL = "http://localhost:8001"

@app.get("/")
async def index(request: Request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{SERVICE_B_URL}/items")
        # response: httpx.Response
        items = response.json()

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "items": items}
    )



