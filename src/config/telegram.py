from pydantic_settings import BaseSettings, SettingsConfigDict


class TelegramSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="TG_SENDER_TG_")
    bot_token: str
    chat_id: int
    message_thread_id: str


telegram_settings = TelegramSettings()
