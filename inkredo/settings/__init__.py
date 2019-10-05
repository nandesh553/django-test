import os

if os.environ.get('ENVIRONMENT') == 'local':
    from .local import *
elif os.environ.get('ENVIRONMENT') == 'production':
    from .production import *
