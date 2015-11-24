from django.shortcuts import render
from news.models import Latestnews

def news(request):
    latestnewss = Latestnews.objects.order_by('-uploadDate')
    context = {'latestnewss':latestnewss}
    return render(request, 'news/news.html', context)

def latestnews(request, latestnewsID):
    context = {}
    try:
        latestnews = Latestnews.objects.get(id=latestnewsID)
        context['latestnews'] = latestnews
    except Latestnews.DoesNotExist:
        pass
    return render(request, 'news/latestnews.html', context)