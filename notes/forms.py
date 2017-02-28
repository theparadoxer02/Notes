from django import forms
from .models import Note

class notesform(forms.ModelForm):
	class Meta:
		model = Note
		fields = [ 'picture','year','branch','subject_name','unit' ]


class EmailForm(forms.Form):
	subject = forms.CharField(required=True,max_length=20)
	names = forms.CharField(required=True)
	email = forms.EmailField()

class searchform(forms.ModelForm):
	class Meta:
		model = Note
		fields = [ 'year','branch','subject_name','unit']