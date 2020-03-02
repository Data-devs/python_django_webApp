
import scrapy as sc
import django as dj

def ShowModules():
    print(' ++++++ Modules on app +++++')
    print('scrapy version : ', sc.version_info)
    print('django version' , dj.__version__)


ShowModules()