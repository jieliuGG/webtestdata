"""
Django settings for webtestdata project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys   #导入sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #获取项目根目录
sys.path.insert(0,BASE_DIR)  #配置apps路径
sys.path.insert(0,os.path.join(BASE_DIR, 'apps'))  #配置apps路径
sys.path.insert(0,os.path.join(BASE_DIR, 'extra_apps'))  #配置apps路径


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%tkkt3-^zy9*$xq6(r@4_irpc9_-f02&(^nxys9pj9ac(_@&_b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']  #在这里请求的host添加了*可以使用域名访问


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'xadmin',  # 注册xadmin
    'crispy_forms',  # 注册xadmin的依赖应用crispy_forms
    'pageelement.apps.PageelementConfig',   #注册pageelement
    'testfundata.apps.TestfundataConfig',   #注册testfundata
    'logindata.apps.LogindataConfig',   #注册logindata
    'searchdata.apps.SearchdataConfig',   #注册searchdata
    'addmerchant.apps.AddmerchantConfig',  # 注册addmerchant


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webtestdata.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'webtestdata.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# DATABASES = {   #数据库配置
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'webdata',
#         'USER':'root',
#         'PASSWORD':'root',
#         'HOST':'127.0.0.1',
#         'OPTIONS':{'init_command':'SET storage_engine=INNODB;'}  #设置数据库为INNODB，为第三方数据库登录用
#     }
# }

DATABASES = {   #数据库配置
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'web_data',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'127.0.0.1',
        'OPTIONS':{'init_command':'SET storage_engine=INNODB;'}  #设置数据库为INNODB，为第三方数据库登录用
    }
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


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True

#设置时区
LANGUAGE_CODE = 'zh-hans'  #中文支持，django1.8以后支持；1.8以前是zh-cn
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False   #默认是Ture，时间是utc时间，由于我们要用本地时间，所用手动修改为false！！！！


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# STATIC_URL = '/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]   #将static加入python跟搜索路径


#Web元素URL域名配置
#测试环境域名
# WEB_URL_TITLE = 'https://bjw.halodigit.com:9090'
WEB_URL_TITLE = 'https://bjw.halodigit.com:9060'
AGENT_REVISE_MERCHANTID = "1002113"
AGENT_DETAILS_MERCHANTID = "1002107"
AGENT_CONTRAT_MERCHANID = "1002213"
AGENT_LOGIN_ACCOUNT = "81122336666"
AGENT_LOGIN_PASSWORD = "abc123456"
#现网域名
# WEB_URL_TITLE = 'https://m-mbmpay.ahdipay.com'
