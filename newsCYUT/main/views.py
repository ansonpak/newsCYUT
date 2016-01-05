from django.shortcuts import render
from news.models import Latestnews

def main(request):
    latestnewss = Latestnews.objects.order_by('-uploadDate')[:5]
    context = {'latestnewss':latestnewss}
    return render(request, 'main/main.html', context)
