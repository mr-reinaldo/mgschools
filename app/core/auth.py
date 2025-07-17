from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from jwt import encode

from app.core.config import Settings

settings = Settings()


def create_access_token(data: dict) -> str:
    """Cria um token de acesso JWT."""
    to_encode = data.copy()
    expire = datetime.now(tz=ZoneInfo(settings.TIMEZONE)) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({'exp': expire})

    encoded_data = encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_data
