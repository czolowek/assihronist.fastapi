from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# Список для хранения имен
names = []

# Модель для валидации входных данных
class NameModel(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="Имя пользователя")

@app.post("/add_name/", summary="Добавить имя", response_description="Имя успешно добавлено")
async def add_name(name_model: NameModel):
    name = name_model.name.strip()
    if name in names:
        raise HTTPException(status_code=400, detail="Имя уже существует")
    names.append(name)
    return {"message": f"Имя '{name}' добавлено"}

@app.get("/get_names/", summary="Получить список имен", response_model=List[str])
async def get_names():
    return names

@app.delete("/delete_name/", summary="Удалить имя", response_description="Имя успешно удалено")
async def delete_name(name_model: NameModel):
    name = name_model.name.strip()
    if name not in names:
        raise HTTPException(status_code=404, detail="Имя не найдено")
    names.remove(name)
    return {"message": f"Имя '{name}' удалено"}


































