# -*- encoding:utf-8 -*-

import os

'''
http://dashboard.daovoice.io/#/app/{your_app_uuid}/apps/settings/open-api
you can find your access_token

'''
DAOVOICE_ACCESS_TOKEN = os.getenv("DAOVOICE_ACCESS_TOKEN")

'''
http://docs.daovoice.io/api/#获取管理员列表

'''

DAOVOICE_DEFAULT_ADMIN_ID = os.getenv("DAOVOICE_DEFAULT_ADMIN_ID")

DAOVOICE_API = os.getenv("DAOVOICE_API", "https://api.daovoice.io")
