from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from server.auth.auth_bearer import JWTBearer


from server.collections.colors import (
    add_color,
    retrieve_colors
)

from server.models.colors import (
    ErrorResponseModel,
    ResponseModel,
    ColorSchema,
    UpdateColorModel
)

router = APIRouter()

@router.get("/colors", dependencies=[Depends(JWTBearer())], response_description="Colors retrieved")
async def get_colors():
    colors = await retrieve_colors()
    if colors:
        return ResponseModel(colors, "Colors data retrieved successfully")
    return ResponseModel(colors, "Empty list returned")

@router.post("/colors", dependencies=[Depends(JWTBearer())], response_description="Color data added into the database")
async def add_color_data(color: ColorSchema = Body(...)):
    color = jsonable_encoder(color)
    new_color = await add_color(color)
    return ResponseModel(new_color, "Color added successfully")
