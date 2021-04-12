from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from server.auth.auth_handler import sing_in

from server.collections.users import (
    add_new_user,
    retrieve_user_by_email,
    verify_password
)

from server.models.users import (
    UserLoginSchema,
    UserSchema,
    ResponseModel,
    ErrorResponseModel
)

router = APIRouter()


@router.post("/singup", response_description="User data added into the database")
async def create_user(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    user_db = await retrieve_user_by_email(user["email"])
    if user_db:
        raise HTTPException(status_code=400, detail=ErrorResponseModel(user, 400, "User already in database"))
    new_user = await add_new_user(user)
    return ResponseModel(new_user, "User added successfully")

@router.post("/login", response_description="User login")
async def user_login(user: UserLoginSchema = Body(...)):
    user = jsonable_encoder(user)
    user_db = await retrieve_user_by_email(user["email"])
    if user_db:
        password_db = user_db["password"]
        if verify_password(user["password"], password_db):
            return sing_in(user_db["email"])
    raise HTTPException(status_code=404, detail=ErrorResponseModel(user, 404, "User data not found"))
