from inkredo.settings.base import *

DEBUG = True

#################################################### Static
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]