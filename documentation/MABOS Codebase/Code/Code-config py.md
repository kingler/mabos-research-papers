# Code: config.py

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # System settings
    MAX_AGENTS = int(os.getenv('MAX_AGENTS', 100))
    DEFAULT_AGENT_TYPE = os.getenv('DEFAULT_AGENT_TYPE', 'reactive')
    PERFORMANCE_TRACKING_INTERVAL = int(os.getenv('PERFORMANCE_TRACKING_INTERVAL', 60))  # seconds

    # Database settings
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = int(os.getenv('DB_PORT', 5432))
    DB_NAME = os.getenv('DB_NAME', 'mas_db')
    DB_USER = os.getenv('DB_USER', 'mas_user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')

    # API settings
    API_HOST = os.getenv('API_HOST', '0.0.0.0')
    API_PORT = int(os.getenv('API_PORT', 8000))
    API_DEBUG = os.getenv('API_DEBUG', 'False').lower() == 'true'

    # Logging settings
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'mas.log')

    # Security settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    JWT_EXPIRATION_DELTA = int(os.getenv('JWT_EXPIRATION_DELTA', 3600))  # seconds

    # Agent communication settings
    MESSAGE_BROKER_URL = os.getenv('MESSAGE_BROKER_URL', 'redis://localhost:6379/0')

    # External service integration
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', '')
    MONITORING_SERVICE_URL = os.getenv('MONITORING_SERVICE_URL', '')

    @staticmethod
    def get_database_url():
        return f"postgresql://{Config.DB_USER}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"

# You can add more configuration classes for different environments
class DevelopmentConfig(Config):
    API_DEBUG = True

class ProductionConfig(Config):
    API_DEBUG = False

class TestingConfig(Config):
    DB_NAME = 'mas_test_db'
    API_DEBUG = True

# Set the active configuration based on the environment
active_config = globals()[f"{os.getenv('ENV', 'Development')}Config"]
```