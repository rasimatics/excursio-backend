import os

def get_settings():
    env = os.getenv("ENV", "dev")
    if env == "prod":
        from .prod import ProductionSettings
        return ProductionSettings()
    else:
        from .dev import DevelopmentSettings
        return DevelopmentSettings()

app_settings = get_settings()

