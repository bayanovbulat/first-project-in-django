from django.db import models

# Create your models here.
class FileModel(models.Model):
	number = models.CharField(max_length = 60)
	file = models.FileField(upload_to="firstapp/static/")
def __unicode__(self):
	return self.name


class Graphs(models.Model):
	name = models.TextField(max_length=60)
	text = models.TextField(max_length=60)
	#image = models.ImageField(null=True,blank=True,upload_to="media/",verbose_name='picture')
	def __unicode__(self):
		return self.name
