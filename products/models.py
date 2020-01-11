from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
	title = models.CharField(max_length=225)
	tel_number = models.CharField(max_length=225)
	pub_date = models.DateTimeField(auto_now=False)
	stars = models.IntegerField(default=1)
	description = models.TextField()
	images = models.FileField(upload_to='images/')
	price = models.CharField(max_length=225)
	address = models.CharField(max_length=225)
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def summary(self):
		return self.description[:100]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')