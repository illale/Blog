from django.db import models

# Create your models here.
class Article(models.Model):
	article_header = models.CharField(max_length=200, default="Defualt")
	article_text = models.TextField()
	article_date = models.DateTimeField()
	article_image = models.ImageField(upload_to="images", blank=True)

	def __str__(self):
		return self.article_header

class Comment(models.Model):
	comment_date = models.DateTimeField()
	comment_text = models.CharField(max_length=600)
	commentor_name = models.CharField(max_length=50)

	def __str__(self):
		return self.commentor_name
