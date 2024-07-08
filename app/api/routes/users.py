# FastAPI routes for users
import traceback
from fastapi import APIRouter, Depends, HTTPException
from app.api.dependencies import get_user_service, get_current_user
from app.api.schemas import user as user_schema
from app.domain.services import UserService
from app.domain.models import User

router = APIRouter()


@router.post("/", response_model=user_schema.User)
async def create_user(user: user_schema.UserCreate, user_service: UserService = Depends(get_user_service)):
    try:
        user = await user_service.create_user(user)
    except Exception as e:
        # print stacktrace
        traceback.print_exc()

        raise HTTPException(status_code=400, detail=str(e))
    return user


@router.get("/me", response_model=user_schema.User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
