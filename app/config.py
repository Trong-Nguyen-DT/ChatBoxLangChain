
from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    open_ai_api_key: str
    weather_key: str
    weather_host: str
    app_host: str
    app_port: int
    api_v1: str
    
appConfig = AppConfig()

OPEN_AI_API_KEY = appConfig.open_ai_api_key
WEATHER_KEY = appConfig.weather_key
WEATHER_HOST = appConfig.weather_host
APP_HOST = appConfig.app_host
APP_PORT = appConfig.app_port
API_V1 = appConfig.api_v1
    