"""
Django settings for boottest project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


from boottest import local_dict

# LOGIN_URL，未登录时重定向到的 URL
LOGIN_URL = local_dict["url"]["login_url"]
# LOGIN_URL = 'http:localhost:8000/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "k+8az5x&aq_!*@%v17(ptpeo@gp2$u-uc30^fze3u_+rqhb#@9"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_apscheduler",
    "app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    #'django.middleware.csrf.CsrfViewMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "boottest.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = "boottest.wsgi.application"
AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.AllowAllUsersModelBackend"]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
DATABASES = {
    # 使用自己的数据库的时候请修改这里的配置
    # 注意underground数据库需要事先创建
    # mysql -u root -p
    # create database underground charset='utf8mb4';
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": local_dict["database"]["NAME"],
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "USER": local_dict["database"]["USER"],
        "PASSWORD": local_dict["database"]["PASSWORD"],
        'OPTIONS': {
            'charset': 'utf8mb4',
        #     "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# 加快测试时的数据导入速度，降低加密算法的迭代次数
# 正式上线时要去掉这里！如果先导入数据再修改hasher可能会出现账号无法登录！
# if DEBUG:
#     PASSWORD_HASHERS = [
#         "boottest.hasher.MyPBKDF2PasswordHasher",
#     ]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'


LANGUAGE_CODE = "zh-Hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

# USE_TZ限制了Datetime等时间Field被存入数据库时是否必须包含时区信息
# 这导致定时任务和常用的datetime.now()等无时区时间在存入时被强制-8h转化为UTC时间
# 从而使数据库可读性差，存储前需要强制增加时区信息，且发送消息容易出错
# 从数据库取出的数据将是有时区信息的，几乎与datetime.now()不可比
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
    },
}
'''