# Global settings for unit tests
import pytest
from app.domain.services import ItemService, UserService
from app.db.SqlDbContext import SqlDbContext
from app.db.database import Base, engine
from app.main import app
from fastapi.testclient import TestClient
from app.core.config import Settings

# Creates in-memory sqlite database for unit tests
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"


@pytest.fixture()
def override_settings():
    new_settings = Settings(DATABASE_URL=SQLALCHEMY_DATABASE_URL)

    app.state.settings = new_settings

    yield


@pytest.fixture(scope="function")
def item_service(override_settings):
    return ItemService(SqlDbContext())


@pytest.fixture(scope="function")
def user_service(override_settings):
    return UserService(SqlDbContext())


@pytest.fixture()
def client(override_settings):
    Base.metadata.create_all(bind=engine)

    """def override_get_user_service():
        return UserService(SqlDbContext())

    def override_get_item_service():
        return ItemService(SqlDbContext())

    app.dependency_overrides[get_user_service] = override_get_user_service
    app.dependency_overrides[get_item_service] = override_get_item_service"""

    client = TestClient(app)
    yield client
    Base.metadata.drop_all(bind=engine)  
    app.dependency_overrides.clear()
