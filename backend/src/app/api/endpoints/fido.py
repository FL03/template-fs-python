"""
    Appellation: auth
    Contributors: FL03 <jo3mccain@icloud.com> (https://gitlab.com/FL03)
    Description:
        ... Summary ...
"""
from fastapi import APIRouter, Depends, HTTPException, Security, status
from fastapi.security.oauth2 import SecurityScopes, OAuth2PasswordRequestForm
from fido2.webauthn import PublicKeyCredentialRpEntity, PublicKeyCredentialUserEntity
from fido2.server import Fido2Server

from app.core import Authorization, session
from app.data.models import User, UserIn, Users, Token, TokenIn

router = APIRouter(tags=['auth', 'fido'])
sesh = session()

rp = PublicKeyCredentialRpEntity(name="FIDO Server", id="localhost")
server = Fido2Server(rp)

credentials = []

@router.get("/")
async def index():
    return redirect("")

@router.post("/register")
async def registration():
    options, state = server.register_begin(
        PublicKeyCredentialUserEntity(
            id=b"user_id",
            name="a_user",
            display_name="A. User",
        ),
        credentials,
        user_verification="discouraged",
        authenticator_attachment="cross-platform",
    )

    session["state"] = state
    print("\n\n\n\n")
    print(options)
    print("\n\n\n\n")

    return jsonify(dict(options))

@router.post("/api/register/complete")
async def register_complete():
    response = request.json
    print("RegistrationResponse:", response)
    auth_data = server.register_complete(session["state"], response)

    credentials.append(auth_data.credential_data)
    print("REGISTERED CREDENTIAL:", auth_data.credential_data)
    return jsonify({"status": "OK"})


@router.post("/auth/fido")
async def authenticate_begin():
    if not credentials:
        abort(404)

    options, state = server.authenticate_begin(credentials)
    session["state"] = state

    return jsonify(dict(options))


@router.post("/auth/fido/redirect")
async def authenticate_complete():
    if not credentials:
        abort(404)

    response = request.json
    print("AuthenticationResponse:", response)
    server.authenticate_complete(
        session.pop("state"),
        credentials,
        response,
    )
    print("ASSERTION OK")
    return jsonify({"status": "OK"})