from django.db import models
from django.contrib.auth.models import User


class ChatApp(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User)
	message = models.CharField(max_length=200,default='')

	def __str__(self):
		return self.message

