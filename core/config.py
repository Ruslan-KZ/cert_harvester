from  pydantic_settings import BaseSttings, SettigsConfigDict
from core.config import BasePath
from dotenv import load_dotenv 

load_dotenv(dotenv_path=f"{BasePath}/.env", override=True)

class Settings(BaseSttings):
    model_config = SettigsConfigDict(
        env_file=f"{BasePath}/.env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    DB_HOST: str
    DB_PORT: str
    DB_PASS: str
    DB_USER: str
    DB_NAME: str
    TOKEN_SECRET_KEY: str   

    @property
    def DATABASE_URL_asyncpg(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    # @property
    # def DATABASE_URL_psycopg2(self) -> str:
    #     return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
