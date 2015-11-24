import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsCYUT.settings')
import django
django.setup()
from news.models import Latestnews
import datetime

def populate():
    latestnews = addLatestnews('abcd', 'defg', datetime.datetime.today())
    

def addLatestnews(title,content,uploadDate):
    latestnews = Latestnews.objects.get_or_create(title=title,content=content,uploadDate=uploadDate)[0]
    return latestnews

if __name__ == '__main__':
    print('開始填入資料...')
    populate()
    print('完成。') 
