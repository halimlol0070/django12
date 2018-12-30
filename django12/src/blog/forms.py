from .models import Post
from django.forms.models import ModelForm
from django import forms
class PostForm(ModelForm):
    #해당 <input>을 사용자가 필수로 입력하지 않아도 되는 공간 설정
    #ClearableFileInput: <input type='file'>형태의 입력공간에 추가설정을 할때 사용하는 위젯
    files=forms.FileField(required=False,widget=forms.ClearableFileInput(attrs={'multiple':True}))
    images=forms.ImageField(required=False,widget=forms.ClearableFileInput(attrs={'multiple':True}))                                                                    
    
    
    class Meta:
        model=Post
        fields=['type','headline','content']
class SearchForm(forms.Form):
    search_word=forms.CharField(max_length=200, label='검색어')


