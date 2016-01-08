from django.shortcuts import render, redirect
from news.models import Latestnews
from django.conf import settings

def main(request):
    latestnewss = Latestnews.objects.order_by('-uploadDate')[:5]
    context = {'latestnewss':latestnewss}
    return render(request, 'main/main.html', context)

def admin_required(fun):
    def auth(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect(settings.LOGIN_URL)
        if request.user.username!='admin':
            return render(request, 'main/main.html')
        return fun(request, *args, **kwargs)
    return auth
