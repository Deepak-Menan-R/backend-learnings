from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Health Service point"
    debug: bool = True
    OpenAPI_KEY = "sk-..."

settings = Settings()
