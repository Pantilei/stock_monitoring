from app.api.api_v1.api import api_router
from app.core.config import settings
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=settings.OPENAPI_URL,
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc")


if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"]
    )

app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host=settings.HOST,
                reload=True, port=settings.PORT)
