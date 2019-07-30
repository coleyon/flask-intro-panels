# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from environs import Env
from os import environ as osenv

env = Env()
selectable_envfilename = osenv.get('ENV_FILE_NAME', default='.env')
env.read_env(selectable_envfilename, recurse=False)

# --------------------------------------------------
# Systems
# --------------------------------------------------
TZ = env.str('TZ', default='Asia/Tokyo')
GUNICORN_WORKERS = env.str('GUNICORN_WORKERS', default='1')
LOG_LEVEL = env.str('LOG_LEVEL', default='debug')

# --------------------------------------------------
# Flask
# --------------------------------------------------
ENV = env.str('FLASK_ENV', default='development')
NODE_ENV = env.str('NODE_ENV', default='development')
DEBUG = ENV == 'development'
SECRET_KEY = env.str('SECRET_KEY')
SEND_FILE_MAX_AGE_DEFAULT = env.int('SEND_FILE_MAX_AGE_DEFAULT', default=43200)

# --------------------------------------------------
# Flask-Bcrypt https://flask-bcrypt.readthedocs.io/en/latest/
# --------------------------------------------------
BCRYPT_LOG_ROUNDS = env.int('BCRYPT_LOG_ROUNDS', default=13)


# --------------------------------------------------
# Flask-DebugToolbar https://flask-debugtoolbar.readthedocs.io/en/latest/#configuration
# --------------------------------------------------
DEBUG_TB_ENABLED = env.str('DEBUG_TB_ENABLED', default='')
DEBUG_TB_INTERCEPT_REDIRECTS = env.bool('DEBUG_TB_INTERCEPT_REDIRECTS', default=False)
# DEBUG_TB_PANELS = env.str('DEBUG_TB_PANELS', default='flask_debugtoolbar.panels.versions.VersionDebugPanel,flask_debugtoolbar.panels.timer.TimerDebugPanel,flask_debugtoolbar.panels.headers.HeaderDebugPanel,flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel,flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel,flask_debugtoolbar.panels.template.TemplateDebugPanel,flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel,flask_debugtoolbar.panels.logger.LoggingPanel,flask_debugtoolbar.panels.route_list.RouteListDebugPanel,flask_debugtoolbar.panels.profiler.ProfilerDebugPanel')
DEBUG_TB_PROFILER_ENABLED = env.bool('DEBUG_TB_PROFILER_ENABLED', default=False)


# --------------------------------------------------
# Flask-SQLAlchemy https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#configuration
# --------------------------------------------------
# Single DB
SQLALCHEMY_DATABASE_URI = env.str('SQLALCHEMY_DATABASE_URI', default=None)
# Multiple DB
SQLALCHEMY_BINDS = None
if SQLALCHEMY_DATABASE_URI is None:
    db_bind_keys = env.list('DB_BIND_KEYS', subcast=str)
    SQLALCHEMY_BINDS = {}
    for idx, key in enumerate(db_bind_keys):
        SQLALCHEMY_BINDS[key] = env.list('DB_CONSTRS', subcast=str)[idx].format(
            user=env.list('DB_USERS', default='', subcast=str)[idx],
            passwd=env.list('DB_PASSWORDS', default='', subcast=str)[idx],
            host=env.list('DB_HOSTS', default='', subcast=str)[idx],
            port=env.list('DB_PORTS', default='', subcast=int)[idx],
            dbname=env.list('DB_DBNAMES', default='', subcast=str)[idx],
            charset=env.list('DB_CHARSETS', default='', subcast=str)[idx],
        )

SQLALCHEMY_ECHO = env.bool('SQLALCHEMY_ECHO')
SQLALCHEMY_TRACK_MODIFICATIONS = env.bool('SQLALCHEMY_TRACK_MODIFICATIONS', False)


# --------------------------------------------------
# Flask-Webpack https://github.com/nickjj/flask-webpack#settings
# --------------------------------------------------
WEBPACK_MANIFEST_PATH = env.str('WEBPACK_MANIFEST_PATH', default='webpack/manifest.json')
# WEBPACK_ASSETS_URL = env.str('WEBPACK_ASSETS_URL', default='')


# --------------------------------------------------
# Flask-Cache https://flask-caching.readthedocs.io/en/latest/index.html#configuring-flask-caching
# --------------------------------------------------
CACHE_TYPE = env.str('CACHE_TYPE', defalut='null')  # Can be "memcached", "redis", etc.
# CACHE_NO_NULL_WARNING = env.str('CACHE_NO_NULL_WARNING', defalut='')
# CACHE_ARGS = env.str('CACHE_ARGS', defalut='')
# CACHE_OPTIONS = env.str('CACHE_OPTIONS', defalut='')
# CACHE_DEFAULT_TIMEOUT = env.str('CACHE_DEFAULT_TIMEOUT', defalut='')
# CACHE_IGNORE_ERRORS = env.str('CACHE_IGNORE_ERRORS', defalut='')
# CACHE_THRESHOLD = env.str('CACHE_THRESHOLD', defalut='')
# CACHE_KEY_PREFIX = env.str('CACHE_KEY_PREFIX', defalut='')
# CACHE_UWSGI_NAME = env.str('CACHE_UWSGI_NAME', defalut='')
# CACHE_MEMCACHED_SERVERS = env.str('CACHE_MEMCACHED_SERVERS', defalut='')
# CACHE_MEMCACHED_USERNAME = env.str('CACHE_MEMCACHED_USERNAME', defalut='')
# CACHE_MEMCACHED_PASSWORD = env.str('CACHE_MEMCACHED_PASSWORD', defalut='')
# CACHE_REDIS_HOST = env.str('CACHE_REDIS_HOST', defalut='')
# CACHE_REDIS_PORT = env.str('CACHE_REDIS_PORT', defalut='')
# CACHE_REDIS_PASSWORD = env.str('CACHE_REDIS_PASSWORD', defalut='')
# CACHE_REDIS_DB = env.str('CACHE_REDIS_DB', defalut='')
# CACHE_REDIS_SENTINELS = env.str('CACHE_REDIS_SENTINELS', defalut='')
# CACHE_REDIS_SENTINEL_MASTER = env.str('CACHE_REDIS_SENTINEL_MASTER', defalut='')
# CACHE_DIR = env.str('CACHE_DIR', defalut='')
# CACHE_REDIS_URL = env.str('CACHE_REDIS_URL', defalut='')

