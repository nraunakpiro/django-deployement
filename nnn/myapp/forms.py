from django import forms
from myapp.models import mdl
class frm(forms.ModelForm):
	class Meta():
		model=mdl
		fields='__all__'