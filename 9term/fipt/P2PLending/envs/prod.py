from P2PLending.envs.local import *

DEBUG = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = ENV_TOKENS.get("EMAIL_LOGIN", None)
EMAIL_HOST_PASSWORD = ENV_TOKENS.get("EMAIL_PASSWORD", None)
EMAIL_PORT = 587
EMAIL_USE_TLS = True