# Implementation of the IDbContext interface using SQLAlchemy
import random
from sqlalchemy.orm import sessionmaker, Session
from typing import List, Type
from app.domain.IDbContext import IDbContext
from app.domain.models import User
from app.domain.models import Item
from app.db.database import engine


class SqlDbContext(IDbContext):
    def __init__(self):
        self.SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.session = self.SessionFactory()

        # Create tables
        User.__table__.create(engine, checkfirst=True)
        Item.__table__.create(engine, checkfirst=True)

    def persist_user(self, user) -> User:
        # auto generate id , random integer
        new_user_id = random.randint(1, 1000)
        db_user = User(id=new_user_id, email=user.email, hashed_password=user.password)
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def persist_item(self, item, user_id) -> Item:
        db_item = Item(**item.dict())
        db_item.owner_id = user_id
        self.session.add(db_item)
        self.session.commit()
        self.session.refresh(db_item)
        return db_item

    def retrieve_user(self, user_id) -> User:
        return self.session.query(User).filter(User.id == user_id).first()

    def retrieve_items(self, skip: int = 0, limit: int = 100) -> List[Item]:
        result = self.session.query(Item).offset(skip).limit(limit).all()
        list_to_return = []
        for item in result:
            # convert to domain model
            it = Item(id=item.id, title=item.title, description=item.description, owner_id=item.owner_id)
            list_to_return.append(it)
        return list_to_return

    def get_session(self) -> Session:
        return self.session

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def close(self) -> None:
        self.session.close()

    def query(self, entity: Type) -> List:
        return self.session.query(entity).all()