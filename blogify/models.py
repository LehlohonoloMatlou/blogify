from django.db import models
from django.contrib.auth.models import User


class Audience(models.Model):
	name = models.CharField(max_length = 35)
	description = models.CharField(max_length = 150)

	class Meta:
		db_table = 'Audience'

	def __str__(self):
		return self.name


class Article(models.Model):
	title = models.CharField(max_length = 35,unique = True)
	context_image = models.ImageField(upload_to = 'context_images')
	description = models.CharField(max_length = 150,null = True) #for admin
	body = models.TextField()
	active = models.BooleanField(default = False)
	last_modified = models.DateField(auto_now = True)
	audience = models.ForeignKey(Audience, on_delete = models.SET_NULL,null = True,blank = True)
	author = models.ForeignKey(User,on_delete = models.SET_NULL,null= True,blank= True)

	class Meta:
		db_table = 'Article'

	# Ensure that only articles with a defined audience,context image and author can be published
	def save(self):
		if self.audience == None or self.author == None or self.context_image == None:
			self.active = False

		super(Article, self).save()

	def __str__(self):
		return self.title
		