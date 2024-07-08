# FastAPI routes for items
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.api.dependencies import get_current_user
from app.api.schemas import item as item_schema
from app.domain.services import ItemService
from app.domain.models import User
from app.db.SqlDbContext import SqlDbContext

router = APIRouter()


def get_item_service():
    return ItemService(SqlDbContext())


@router.post("/", response_model=item_schema.Item)
async def create_item(
        item: item_schema.ItemCreate,
        item_service: ItemService = Depends(get_item_service),
        current_user: User = Depends(get_current_user)
):
    try:
        item = await item_service.create_item(item, current_user.id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return item


@router.get("/", response_model=List[item_schema.Item])
async def read_items(skip: int = 0, limit: int = 100, item_service: ItemService = Depends(get_item_service)):
    try:
        items = await item_service.get_items(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return items
