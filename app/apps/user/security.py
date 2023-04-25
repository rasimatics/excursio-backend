from passlib.context import CryptContext
from datetime import timedelta, datetime
from jose import jwt
from app.core.config.settings import app_settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def hash_password(plain_password: str):
    """
        hash password
    """
    return pwd_context.hash(plain_password)


def check_password(plain_passowrd: str, hash_password: str):
    """
        check password
    """
    return pwd_context.verify(plain_passowrd, hash_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
        jwt token generation
    """
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=app_settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, app_settings.SECRET_KEY, algorithm=app_settings.ALGORITHM)
    return encoded_jwt

    

