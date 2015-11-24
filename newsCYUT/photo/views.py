from django.shortcuts import render

def photo(request):
    return render(request, 'photo/photo.html')