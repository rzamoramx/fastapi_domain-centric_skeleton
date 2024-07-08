# implements business logic
from app.api.schemas import user as user_schema, item as item_schema
from app.domain.IDbContext import IDbContext


class UserService:
    def __init__(self, db_context: IDbContext):
        self.db_context = db_context

    async def create_user(self, user: user_schema.UserCreate):
        # Business logic here like rules, validations, etc.

        new_user = self.db_context.persist_user(user)

        # Convert domain User into schema User
        user = user_schema.User(id=new_user.id, email=new_user.email, password=new_user.hashed_password)

        return user

    async def get_user(self, user_id: int):
        # Business logic here like rules, validations, etc.

        return self.db_context.retrieve_user(user_id)


class ItemService:
    def __init__(self, db_context: IDbContext):
        self.db_context = db_context

    async def create_item(self, item: item_schema.ItemCreate, user_id: int):
        # Business logic here like rules, validations, etc.

        new_item = self.db_context.persist_item(item, user_id)

        # Convert domain Item into schema Item
        item = item_schema.Item(id=new_item.id, title=new_item.title, description=new_item.description, owner_id=new_item.owner_id)

        return item

    async def get_items(self, skip: int = 0, limit: int = 100):
        # Business logic here like rules, validations, etc.

        return self.db_context.retrieve_items(skip, limit)