from django.db import models

# Create your models here.
class Article(models.Model):
	article_text = models.TextField()
	article_date = models.DateTimeField()

	def __str__(self):
		return self.article_text
