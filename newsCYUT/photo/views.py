from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from photo.models import Album, Photo
from photo.forms import AlbumForm, PhotoForm


def photobook(request):
    albums = Album.objects.order_by()
    context = {'albums':albums}
    return render(request, 'photo/photobook.html', context)

def album(request, albumID):
    context = {}
    try:
        album = Album.objects.get(id=albumID)
        context['album'] = album
        context['photos'] = Photo.objects.filter(album=album)
    except Album.DoesNotExist:
        pass
    return render(request, 'photo/album.html', context)

def photo(request, photoID):
    context = {}
    try:
        photo = Photo.objects.get(id=photoID)
        context['photo'] = photo
    except Photo.DoesNotExist:
        pass
    return render(request, 'photo/photo.html', context)

def addAlbum(request):
    template = 'photo/addAlbum.html'
    if request.method=='GET':
        return render(request, template, {'form':AlbumForm()})
    form = AlbumForm(request.POST)
    if not form.is_valid():
        return render(request, template, {'form':form})
    form.save()
    return redirect(reverse('photo:photobook'))

def addPhoto(request, albumID):
    template = 'photo/addPhoto.html'
    try:
        photoAlbum = Album.objects.get(id=albumID)
    except Album.DoesNotExist:
        return album(request, albumID)
    context = {'album':photoAlbum}
    if request.method=='GET':
        context['form'] = PhotoForm()
        return render(request, template, context)
    form = PhotoForm(request.POST)
    context['form'] = form
    if not form.is_valid():
        return render(request, template, context)
    photo = form.save(commit=False)
    photo.album = photoAlbum
    photo.save()
    return redirect(reverse('photo:album', args=(albumID, )))

def deleteAlbum1(request):
    albums = Album.objects.all().order_by()
    context = {'albums':albums}
    return render(request, 'photo/deleteAlbum1.html', context)

def deleteAlbum(request, albumID):
    if request.method!='POST':
        return photobook(request)
    albumToDelete = Album.objects.get(id=albumID)
    if albumToDelete:
        albumToDelete.delete()
    return redirect(reverse('photo:deleteAlbum1'))

def deletePhoto1(request):
    photos = Photo.objects.all().order_by()
    context = {'photos':photos}
    return render(request, 'photo/deletePhoto1.html', context)

def deletePhoto(request, photoID):
    if request.method!='POST':
        return photobook(request)
    photoToDelete = Photo.objects.get(id=photoID)
    if photoToDelete:
        albumID = photoToDelete.album.id
        photoToDelete.delete()
    else:
        albmID = ''
    return redirect(reverse('photo:album', args=(albumID, )))

def updateAlbum(request, albumID):
    template = 'photo/updateAlbum.html'
    try:
        album = Album.objects.get(id=albumID)
    except Album.DoesNotExist:
        return photobook(request)
    if request.method=='GET':
        form = AlbumForm(instance=album)
        return render(request, template, {'form':form, 'album':album})
    # request.method=='POST'
    form = AlbumForm(request.POST, instance=album)
    if not form.is_valid():
        return render(request, template, {'form':form, 'album':album})
    form.save()
    return redirect(reverse('photo:photobook'))

def updatePhoto(request, photoID):
    template = 'photo/updatePhoto.html'
    try:
        photo = Photo.objects.get(id=photoID)
    except Photo.DoesNotExist:
        return album(request, '')
    if request.method=='GET':
        form = PhotoForm(instance=photo)
        return render(request, template, {'form':form, 'photo':photo})
    # request.method=='POST'
    form = PhotoForm(request.POST, instance=photo)
    if not form.is_valid():
        return render(request, template, {'form':form, 'photo':photo})
    form.save()
    return redirect(reverse('photo:album', args=(photo.album.id,)))