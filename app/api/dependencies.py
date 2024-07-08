# Dependencies for all routes of the API
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.db.SqlDbContext import SqlDbContext
from app.domain.services import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_user_service():
    return UserService(SqlDbContext())


async def get_current_user(token: str = Depends(oauth2_scheme), user_service: UserService = Depends(get_user_service)):
    user = await user_service.get_user(int(token))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
