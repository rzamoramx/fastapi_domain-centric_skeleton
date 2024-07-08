# Unit tests for user domain service
import pytest
from app.domain.services import UserService
from app.api.schemas.user import UserCreate


@pytest.mark.asyncio
async def test_create_user(user_service):
    user_data = UserCreate(email="test@example.com", password="testpassword")
    user = await user_service.create_user(user_data)
    assert user.email == user_data.email
    assert user.id is not None


@pytest.mark.asyncio
async def test_get_user(user_service):
    user_data = UserCreate(email="test@example.com", password="testpassword")
    created_user = await user_service.create_user(user_data)
    
    retrieved_user = await user_service.get_user(created_user.id)
    assert retrieved_user is not None
    assert retrieved_user.id == created_user.id
    assert retrieved_user.email == created_user.email