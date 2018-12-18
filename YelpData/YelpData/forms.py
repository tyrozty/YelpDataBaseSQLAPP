from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from YelpData.models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'POST'
		self.helper.add_input(Submit('submit', 'submit'))