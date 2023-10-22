# To use Neon with Django, you have to create a Project on Neon and specify the project connection settings in your settings.py in the same way as for standalone Postgres.
from cfehome.env import config
import dj_database_url

DATABASES_URL = config("DATABASE_URL", default= None)
if DATABASES_URL is not None:
  DATABASES = {
    'default': dj_database_url.config(
      default=DATABASES_URL,
      conn_max_age=600,
      conn_health_checks=True,
      ssl_require=True,
    )
  }