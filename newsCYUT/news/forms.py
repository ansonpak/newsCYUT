from django import forms
from news.models import Latestnews

class LatestnewsForm(forms.ModelForm):
    title = forms.CharField(max_length=128, label='最新消息標題', help_text='(請輸入最新消息標題)')
    content = forms.CharField(widget=forms.Textarea, label='最新消息正文')
    uploadDate = forms.DateField(label='最新消息更新時間') 
    
    class Meta:
        model = Latestnews
        fields = ('title', 'content', 'uploadDate')