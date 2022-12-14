from fastapi import APIRouter, HTTPException, status, Depends
from app.models.token import Token, Login
from app.repositories.users import UserRepository
from app.core.security import verify_password, create_access_token
from app.endpoints.depends import get_user_repository

router = APIRouter()


@router.post("/", response_model=Token)
async def login(login: Login, users: UserRepository = Depends(get_user_repository)):
    user = await users.get_by_email(login.email)
    if user is None and verify_password(login.password, user.hashed_password) :
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username or password')
    return Token(
        access_token=create_access_token({'sub': user.email}),
        token_type="Bearer"
    )
