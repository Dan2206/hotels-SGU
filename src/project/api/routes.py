from fastapi import APIRouter

from project.infrastructure.postgres.repository.user_repo import UserRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.schemas.user import UserSchema


router = APIRouter()


@router.get("/all_clients", response_model=list[UserSchema])
async def get_all_clients() -> list[UserSchema]:
    user_repo = UserRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await user_repo.check_connection(session=session)
        all_clients = await user_repo.get_all_clients(session=session)

    return all_clients
