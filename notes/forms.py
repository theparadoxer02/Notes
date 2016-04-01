from django import forms
from .models import Note,Subject


json ={
  'CSE':
  {
    'First':
    {
        'Physics','Chemistry','Electronics','Electrical'
    }
    ,'Second':
    {
        'Operating System', 'Data Structure'
    }
  }
}


class notesform(forms.ModelForm):
	class Meta:
		model = Note
		fields = [ 'picture','unit_no' ]


class EmailForm(forms.Form):
	subject = forms.CharField(max_length=20)
	names = forms.CharField(max_length=20)
	email = forms.EmailField()

class searchform(forms.Form):
	branch = forms.CharField(max_length=10)
	year = forms.CharField(max_length=10)
	subject = forms.CharField(max_length=15)



# class searchform(forms.Form):
# 	def __init__(self,*args,**kwargs):
# 		super(searchform,self).__init__(*args,**kwargs)
# 		self.fields['year']=forms.ChoiceField(
# 		choices=get_my_choices()
# 		)
#
# def get_my_choices():
# 	choices_list = Note.objects.all()
