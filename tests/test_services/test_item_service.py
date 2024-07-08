# Unit tests for item domain service
import pytest
from app.api.schemas.user import UserCreate
from app.api.schemas.item import ItemCreate


@pytest.mark.asyncio
async def test_create_item(item_service, user_service):
    # First create a user
    user_data = UserCreate(email="test@example.com", password="testpassword")
    user = await user_service.create_user(user_data)

    # Then create an item for that user
    item_data = ItemCreate(title="Test Item", description="This is a test item")
    item = await item_service.create_item(item_data, user.id)
    assert item.title == item_data.title
    assert item.description == item_data.description
    assert item.owner_id == user.id


@pytest.mark.asyncio
async def test_get_items(item_service, user_service):
    # Create some items
    user_data = UserCreate(email="test@example.com", password="testpassword")
    user = await user_service.create_user(user_data)
    
    for i in range(5):
        item_data = ItemCreate(title=f"Test Item {i}", description=f"This is test item {i}")
        await item_service.create_item(item_data, user.id)

    items = await item_service.get_items()
    assert len(items) == 6
