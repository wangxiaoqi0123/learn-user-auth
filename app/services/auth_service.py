from app.core.security import create_access_token, create_refresh_token


async def login(username: str, password: str):
    access_token = create_access_token({"sub": 1, "username": username})
    refresh_token = create_refresh_token({"sub": 1})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "user": {
            "id": 1,
            "username": username,
        },
    }
