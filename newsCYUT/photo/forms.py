from django import forms
from photo.models import Album, Photo


class AlbumForm(forms.ModelForm):
    photourl = forms.URLField(max_length=12800, label='相片網址')
    albumtitle = forms.CharField(max_length=128, label='相簿名稱', help_text='(請輸入相簿名稱)')

    class Meta:
        model = Album
        fields = ('photourl', 'albumtitle')
        
class PhotoForm(forms.ModelForm):
    url = forms.URLField(max_length=99999, label='相片網址')
    index = forms.CharField(max_length=12800, label='相片簡介', help_text='(請輸入相片簡介)')
    
    class Meta:
        model = Photo
        fields = ('url', 'index')
                         