from fastapi import Request, File, UploadFile
from fastapi.routing import APIRouter
from io import BytesIO
import pandas as pd

router = APIRouter()

@router.get("/create_batch")
async def root(request: Request):
    return {"message": "Create Batch"}

@router.post("/upload-excel")
async def upload_excel(file: UploadFile = File(...)):
    # Leer el archivo Excel en memoria
    contents = await file.read()
    excel_data = pd.read_excel(BytesIO(contents))  # Convertir en DataFrame
    num_filas = excel_data.shape[0]
    _list = []
    # for index, row in excel_data.iterrows():
    #     _list.append(row.to_dict())
    return {"message": "Archivo procesado correctamente", "filename": file.filename, "data": _list, "num_filas": num_filas}