from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware
from settings import Settings
from src.root.controllers.create_batch import router as create_batch

app = FastAPI(title='Bulk file upload', root_path=Settings.openapi_prefix, description="Bulk file upload")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("")
async def root():
    return {"message": "Bienvenidos al Backend!!!!!"}

app.include_router(create_batch)

handler = Mangum(app)