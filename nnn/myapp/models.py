from django.db import models
class mdl(models.Model):
	name=models.CharField(max_length=245)
	address=models.CharField(max_length=245)
	Mob=models.IntegerField()
# Create your models here.
