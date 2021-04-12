from typing import Optional
from pydantic import BaseModel, Field


class ColorSchema(BaseModel):
    color_usage: str = Field(...)
    color_type: str = Field(...)
    color_hex: str = Field(...)
    
    class Config:
        schema_extra = {
            "example": {
                "color_usage": "class container-principal",
                "color_type": "background-color",
                "color_hex": "#3F94E5"
            }
        }

class UpdateColorModel(BaseModel):
    color_usage: Optional[str]
    color_type: Optional[str]
    color_hex: Optional[str]
    
    class Config:
        schema_extra = {
            "example": {
                "color_usage": "class container-secundario",
                "color_type": "background-color",
                "color_hex": "#3F94E5"
            }
        }
        
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message
    }
    
def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
