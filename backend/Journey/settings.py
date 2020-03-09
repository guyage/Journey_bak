"""
Django settings for Journey project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import configparser
import sys
import datetime
#ldap认证相关
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, PosixGroupType, LDAPGroupQuery, LDAPSearchUnion
#celery相关
import djcelery
from celery.schedules import crontab
from celery.schedules import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'utils'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%^pimvx5^5_#of7cpyxc#j8^3l*an9x7t6=ckt41^61ahavv34'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'user.Users'


MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")
MEDIA_URL = "/uploads/"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_swagger',
    'easyaudit',
    'user',
    'db',
    'conf',
    'query',
    'common',
    # 'workflow',
    # 'sqlorder',
    'charts',
    'workorder',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    #  配置默认的认证方式  帐号密码认证
    'DEFAULT_AUTHENTICATION_CLASSES' : (  
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

# django-easy-audit配置


# swagger 配置项
SWAGGER_SETTINGS = {
    # 基础样式
    'SECURITY_DEFINITIONS': {
        "basic": {
            'type': 'basic'
        }
    },
    # 如果需要登录才能够查看接口文档, 登录的链接使用restframework自带的.
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    # 'DOC_EXPANSION': None,
    # 'SHOW_REQUEST_HEADERS':True,
    # 'USE_SESSION_AUTH': True,
    # 'DOC_EXPANSION': 'list',
    # 接口文档中方法列表以首字母升序排列
    'APIS_SORTER': 'alpha',
    # 如果支持json提交, 则接口文档中包含json输入框
    'JSON_EDITOR': True,
    # 方法列表字母排序
    'OPERATIONS_SORTER': 'alpha',
    'VALIDATOR_URL': None,
}

# JWT_EXPIRATION_DELTA 指明token的有效期
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_RESPONSE_PAYLOAD_HANDLER':'user.utils.jwt_response_payload_handler',
    'JWT_GET_USER_SECRET_KEY': 'user.models.jwt_get_secret_key',
    'JWT_ALLOW_REFRESH': True,
}

ROOT_URLCONF = 'Journey.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Journey.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# 获取配置文件信息
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR,'Journey.conf'))
# djano 数据库连接信息
DB_HOST = config.get('db', 'host')
DB_PORT = config.getint('db', 'port')
DB_USER = config.get('db', 'user')
DB_PASSWORD = config.get('db', 'password')
DB_DATABASE = config.get('db', 'database')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_DATABASE,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# 设置日志,存放路径
# LOG_PATH = 'logs'
# LAST_BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_LOG_DIR = os.path.join(BASE_DIR, "logs")

# 设置日志
LOGGING = {
    'version': 1,  # 保留字
    'disable_existing_loggers': False,  # 禁用已经存在的logger实例
    # 日志文件的格式
    'formatters': {
        # 详细的日志格式
        'standard': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                      '[%(levelname)s][%(message)s]'
        },
        # 简单的日志格式
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        # 定义一个特殊的日志格式
        'collect': {
            'format': '%(message)s'
        }
    },
    # 过滤器
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 处理器
    'handlers': {
        # 在终端打印
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',  #
            'formatter': 'simple'
        },
        # 默认的
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "journey_all.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 3,  # 最多备份几个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 专门用来记错误日志
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "journey_err.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        # 专门定义一个收集特定信息的日志
        'collect': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "journey_collect.log"),
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'collect',
            'encoding': "utf-8"
        }
    },
    'loggers': {
        # 默认的logger应用如下配置
        'default': {
            'handlers': ['default', 'console', 'error'],  # 上线之后可以把'console'移除
            'level': 'DEBUG',
            'propagate': True,  # 向不向更高级别的logger传递
        },
        # 名为 'collect'的logger还单独处理
        'collect': {
            'handlers': ['console', 'collect'],
            'level': 'INFO',
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# ldap认证相关配置
# ladp连接信息(参数在Journey.conf中设置)
LDAP_URI = config.get('ldap', 'ldap_uri')
LADP_BASE_DN = config.get('ldap', 'ldap_base_dn')
LADP_BIND_DN = config.get('ldap', 'ldap_bind_dn')
LADP_BIND_PASSWD = config.get('ldap', 'ldap_bind_passwd')

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = LDAP_URI  # 服务器地址
# ldap查找用户,可以为任一用户
AUTH_LDAP_BIND_DN = LADP_BIND_DN + ',' + LADP_BASE_DN
AUTH_LDAP_BIND_PASSWORD = LADP_BIND_PASSWD
# key为数据库字段名，value为ldap中字段名，此字典解决django model与ldap字段名可能出现的不一致问题
AUTH_LDAP_USER_ATTR_MAP = {
    "username": "sAMAccountName",
    'email': 'mail',
    "first_name": "givenName",
    "last_name": "sn",
}

AUTH_LDAP_USER_SEARCH = LDAPSearch(
    LADP_BASE_DN,
    ldap.SCOPE_SUBTREE,
    '(sAMAccountName=%(user)s)',    
)

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(LADP_BASE_DN,ldap.SCOPE_SUBTREE, "(objectClass=group)" )  #搜索某个OU下组信息
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn") #返回的组的类型，并用来判断用户与组的从属关系
# AUTH_LDAP_MIRROR_GROUPS = True #导入用户的组信息，在用户登录的时候把用户的域组关系同步过来。每次用户登录时，都会把用户的组关系删除，重新从ldap中进行同步（解决办法参考后面）
AUTH_LDAP_ALWAYS_UPDATE_USER = True #是否同步LDAP修改



# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
