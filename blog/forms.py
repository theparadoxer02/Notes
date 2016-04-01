from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',"image","draft")

class EmailForm(forms.Form):
	subject = forms.CharField(required=True,max_length=20)
	names = forms.CharField(required=True)
	email = forms.EmailField()

class CommentForm(forms.ModelForm):
	class Meta:
		model =	Comment
		fields = ('author',	'text',)
