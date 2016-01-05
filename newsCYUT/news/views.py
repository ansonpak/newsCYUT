from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from news.models import Latestnews
from news.forms import LatestnewsForm

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

def addLatestnews(request):
    template = 'news/addLatestnews.html'
    if request.method=='GET':
        return render(request, template, {'form':LatestnewsForm()})
    # request.method=='POST'
    form = LatestnewsForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form':form})
    form.save()
    return redirect(reverse('news:news'))
    # Or try this: return news(request) 
    
def deleteLatestnews1(request):
    latestnewss = Latestnews.objects.all().order_by('-uploadDate')
    context = {'latestnewss':latestnewss}
    return render(request, 'news/deleteLatestnews1.html', context)

def deleteLatestnews(request, latestnewsID):
    if request.method!='POST':
        return news(request)
    # request.method=='POST':
    latestnewsToDelete = Latestnews.objects.get(id=latestnewsID)
    if latestnewsToDelete:
        latestnewsToDelete.delete()
    return redirect(reverse('news:deleteLatestnews1'))