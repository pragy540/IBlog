from django.forms import ModelForm
from .models import Post


class updatePost(ModelForm):
    class Meta:
        model=Post
        fields=['title','content']

