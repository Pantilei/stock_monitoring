from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    HOST: str
    PORT: int

    PROJECT_NAME: str = "Stock Monitoring"
    OPENAPI_URL: str = "/api_v1/openapi.json"

    API_V1_STR: str

    AUTH_SECRET_KEY: str
    HASH_ALGHORITHM: str
    ACCESS_TOKEN_EXPIRE_TIME: int

    SQLALCHEMY_DATABASE_URL: str

    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PASSWORD: str

    class Config:
        case_sensitive = True


settings = Settings()
