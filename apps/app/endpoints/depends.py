from app.repositories.users import UserRepository
from app.db.base import database


def get_user_repository() -> UserRepository:
    return UserRepository(database)
