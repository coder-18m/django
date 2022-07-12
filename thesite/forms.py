from django import forms
from .models import Post, Category, Comment

#choices = [('uncategorized', 'uncategorized'), ('test', 'test'),]
choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'author': forms.Select(attrs={'class': 'form-control', 'style': 'width:100px'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control', 'style': 'width:140px' }),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
