from fastapi import FastAPI
from server.routers.colors import router as ColorRouter
from server.routers.users import router as UserRouter

app = FastAPI()

app.include_router(ColorRouter, tags=["Colors"], prefix="/website")
app.include_router(UserRouter, tags=["Users"], prefix="/website")
