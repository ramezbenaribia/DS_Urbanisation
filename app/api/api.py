from fastapi import APIRouter


from app.api.endpoints import dayOfWeek
from app.api.endpoints import monthOfYear

api_router = APIRouter()


api_router.include_router(dayOfWeek.router, prefix="/api/days", tags=["Day Of Week"])
api_router.include_router(monthOfYear.router, prefix="/api/months", tags=["Month Of the Year"])