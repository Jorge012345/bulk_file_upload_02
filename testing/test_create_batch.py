import pytest
import os
import asyncio
import time
from fastapi.testclient import TestClient
from src.root.main import app  # Importa tu aplicación FastAPI

client = TestClient(app)
BASE_URL = "/upload-excel"

async def upload_excel(results, response_times):
    start_time = time.time()  # Iniciar tiempo
    file_path = os.path.join(os.path.dirname(__file__), "data.xlsx")

    with open(file_path, "rb") as f:
        files = {"file": (file_path, f, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
        response = client.post(BASE_URL, files=files)

    duration = time.time() - start_time  # Calcular duración
    response_times.append(duration)  # Guardar el tiempo de respuesta
    results.append(response.status_code == 200)

@pytest.mark.asyncio
async def test_upload_excel_multiple():
    size = 30
    results = []
    response_times = []
    tasks = [upload_excel(results, response_times) for _ in range(size)]
    await asyncio.gather(*tasks)

    print(f"🔹 Total de solicitudes: {len(results)}")
    print(f"✅ Exitosas: {results.count(True)}")
    print(f"❌ Fallidas: {results.count(False)}")
    print(f"⏳ Tiempo promedio de respuesta: {sum(response_times)/len(response_times):.2f} segundos")

    assert all(results), f"FALLARON {results.count(False)} de {size} solicitudes"