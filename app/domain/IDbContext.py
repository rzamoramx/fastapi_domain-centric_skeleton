# DBContext approach is used to abstract the database operations from the domain layer.
from abc import ABC, abstractmethod
from typing import List, Type
from sqlalchemy.orm import Session
from app.domain.models import User, Item


class IDbContext(ABC):
    @abstractmethod
    def persist_user(self, user) -> User:
        pass

    @abstractmethod
    def persist_item(self, item, user_id) -> Item:
        pass

    @abstractmethod
    def retrieve_user(self, user_id) -> User:
        pass

    @abstractmethod
    def retrieve_items(self, skip: int = 0, limit: int = 100) -> List[Item]:
        pass

    @abstractmethod
    def get_session(self) -> Session:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    @abstractmethod
    def query(self, entity: Type) -> List:
        pass