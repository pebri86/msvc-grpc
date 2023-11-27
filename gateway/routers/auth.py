from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from auth.client import AuthClient

router = APIRouter()


class AuthRequest(BaseModel):
    username: str
    password: str


@router.post("/v1/register")
async def register_user(request: AuthRequest):
    auth_client = AuthClient()
    result = await auth_client.register(
        username=request.username, password=request.password
    )

    return JSONResponse({"success": result.success, "message": result.message})


@router.post("/v1/login")
async def user_login(request: AuthRequest):
    auth_client = AuthClient()
    result = await auth_client.login(
        username=request.username, password=request.password
    )

    return JSONResponse(
        {"success": result.success, "message": result.message, "token": result.token}
    )
