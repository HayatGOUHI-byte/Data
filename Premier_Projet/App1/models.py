from django.db import models
from datetime import date


from django.db import models


class Blog(models.Model):
	name = models.CharField(max_length=100)
	tagline = models.TextField()


	def __str__(self):
		return self.full_name

class Author(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name



class Entry(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	headline = models.CharField(max_length=255)
	body_text = models.TextField()
	pub_date=models.DateField()
	mod_date = models.DateField(default = date.today)
	authors = models.ManyToManyField(Author)


	def __str__(self):
		return self.headline



#Journalist
class Reporter(models.Model):
	full_name = models.CharField(max_length=70)

	def __str__(self):
		return self.full_name



class Article(models.Model):
	pub_date = models.DateField()
	headline = models.CharField(max_length=200)
	content = models.TextField()
	reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

	def __str__(self):
		return self.headline




class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField(Author)

	def __str__(self):
		return self.title



class Title(models.Model):
	titre = models.CharField(max_length=200)

	def __str__(self):
		return self.titre


class Marchandise(models.Model):
	titre= models.CharField(max_length=200)

	def __str__(self):
		return self.titre


class voiture(models.Model):
	brand=models.CharField(max_length=300)




   



