from datetime import datetime

from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware


from app import PROJECT_NAME


from app.api.api import api_router


now = datetime.now()

# We can add a title to our Swagger UI like the project name and the current time
sub_app = FastAPI(
    title=PROJECT_NAME + ' ' + now.strftime("%d/%m/%Y %H:%M:%S"),
    openapi_url=f"/openapi.json",
    docs_url=f"/", redoc_url=f"/",
)

sub_app.add_middleware(GZipMiddleware, minimum_size=1000)

# this method is for including  the router that we are going to use for sending our requests  to the APP
sub_app.include_router(api_router, prefix="")


app = sub_app
