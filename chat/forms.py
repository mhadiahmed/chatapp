from django import forms
from .models import ChatApp

class MessageApp(forms.ModelForm):
	class Meta:
		model = ChatApp
		fields = [
		'message'
		]