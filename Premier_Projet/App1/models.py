from django.db import models
from datetime import date


from django.db import models




class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField("date published")


class Choice(models.Model):
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes=models.IntegerField(default=0)



class Answer(models.Model):
	phrase = models.ForeignKey(Question, on_delete=models.CASCADE)
	phrase2=models.ForeignKey(Question, on_delete=models.CASCADE)
	conclusion = models.PrimaryKey


class Reponse(models.Model):
	return HttpResponse("it s a file to do ")






   



