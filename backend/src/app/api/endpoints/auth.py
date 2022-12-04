"""
    Appellation: auth
    Contributors: FL03 <jo3mccain@icloud.com> (https://gitlab.com/FL03)
    Description:
        ... Summary ...
"""
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, Security, status
from fastapi.security.oauth2 import SecurityScopes, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from pydantic import ValidationError
from typing import Union

from app.core import Authorization, session
from app.data.models import User, UserIn, Users, Token, TokenIn

router = APIRouter(tags=['auth'])
sesh = session()
auth = Authorization()


class Authenticator:
    username: str
    password: str

    async def get_user(self, username: str) -> UserIn:
        self.username = username
        data = await UserIn.from_queryset_single(Users.get(username=username))
        if data: 
            return data

class AccessToken(object):
    data: dict
    expires_delta: Union[timedelta, None] = None

    def __init__(data: dict, expires_delta: Union[timedelta, None] = None, *args, **kwargs):
        self.data = data
        self.expires_delta = expires_delta

    def create(self):
        to_encode = self.data.copy()
        if expires_delta:
            expire = datetime.utcnow() + self.expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, sesh.settings.secret_token, algorithm=auth.algorithm)


async def get_user(username: str) -> UserIn:
    data = await UserIn.from_queryset_single(Users.get(username=username))
    if data:
        return data


async def authenticate_user(username: str, password: str) -> UserIn:
    user = await get_user(username)
    if user and auth.verify_password(password, user.hashed_password):
        return user


def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, sesh.settings.secret_token, algorithm=auth.algorithm)
    return encoded_jwt


async def get_current_user(security_scopes: SecurityScopes, token: str = Depends(auth.scheme)):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f"Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, sesh.settings.secret_token, algorithms=[auth.algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = Token(scopes=token_scopes, username=username)
    except (JWTError, ValidationError):
        raise credentials_exception
    user = await get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user


async def get_current_active_user(current_user: User = Security(get_current_user, scopes=["me"])):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(
        data=dict(sub=user.username, scopes=form_data.scopes),
        expires_delta=timedelta(minutes=auth.expires),
    )
    return Token(access_token=access_token, token_type="bearer")
