from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # LLM
    GROQ_API_KEY: str
    MODEL_NAME: str

    # Email
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    EMAIL_ADDRESS: str
    EMAIL_PASSWORD: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()