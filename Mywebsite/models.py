from django.db import models

# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	subject=models.CharField(max_length=100)
	msg=models.TextField()

	def __str__(self):
		return self.name+" "+self.email


#viren viren
#mayur mayur

class Login(models.Model):
	user=models.CharField(max_length=100)
	password=models.CharField(max_length=100)


	def __str__(self):
		return self.user