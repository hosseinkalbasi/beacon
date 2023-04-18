from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from models.beacon import BeaconData
from fastapi.encoders import jsonable_encoder

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.post("/v1/beacon/", tags=["Beacon Server"], response_model=BeaconData,
          description="Send beacon data to the server")
async def post_beacon(body: BeaconData):
    print(jsonable_encoder(body))
    return body


@app.get("/page/{id}", tags=["Webpage"], response_class=HTMLResponse,
         description="Get a sample page (where user interaction happens)")
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("page.html", {"request": request, "id": id, "title": "Sample Page"})
