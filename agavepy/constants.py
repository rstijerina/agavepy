"""Provides global constants to the AgavePy package
"""
__all__ = [
    'PLATFORM', 'BASE_URL', 'SESSION_CACHE_DIRS', 'CACHE_FILENAME',
    'SESSIONS_FILENAME', 'AGPY_FILENAME', 'CACHES_DIR_NAME', 'ENV_USERNAME',
    'ENV_PASSWORD', 'ENV_TOKEN', 'ENV_REFRESH_TOKEN', 'ENV_BASE_URL',
    'ENV_API_KEY', 'ENV_API_SECRET', 'ENV_TENANT_ID', 'TOKEN_SCOPE',
    'TOKEN_TTL', 'TENANTS_URL'
]

# General
PLATFORM = 'Tapis'
BASE_URL = 'https://api.tacc.utexas.edu'
TENANTS_URL = BASE_URL + '/tenants'

# Variable names usable in lieu of passed values to allow environment-driven
# configuration of the library
ENV_USERNAME = 'TAPIS_USERNAME'
ENV_PASSWORD = 'TAPIS_PASSWORD'
ENV_TOKEN = 'TAPIS_TOKEN'
ENV_REFRESH_TOKEN = 'TAPIS_REFRESH_TOKEN'
ENV_BASE_URL = 'TAPIS_BASE_URL'
ENV_TENANT_ID = 'TAPIS_TENANT_ID'
ENV_API_KEY = 'TAPIS_API_KEY'
ENV_API_SECRET = 'TAPIS_API_SECRET'

# Cache and session maangement
SESSION_CACHE_DIRS = ('TAPIS_CACHE_DIR', 'TAPIS_CACHE', 'AGAVE_CACHE_DIR')
CACHES_DOT_DIR = '.agave'
AGPY_FILENAME = '.agpy'
CACHE_FILENAME = 'current'
SESSIONS_FILENAME = 'config.json'

# Oauth access tokens
TOKEN_SCOPE = 'PRODUCTION'
TOKEN_TTL = 3600
