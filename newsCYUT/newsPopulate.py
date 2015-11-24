import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsCYUT.settings')
import django
django.setup()
from news.models import News
import datetime

def populate():
    news = addNews('abcd', 'defg', datetime.datetime.today())
    

def addNews(title,content,uploadDate):
    news = News.objects.get_or_create(title=title,content=content,uploadDate=uploadDate)[0]
    return news

if __name__ == '__main__':
    print('開始填入資料...')
    populate()
    print('完成。') 
