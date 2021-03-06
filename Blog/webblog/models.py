from django.db import models
from django.forms import ModelForm
from datetime import datetime

# Create your models here.
class Article(models.Model):
	article_header = models.CharField(max_length=200, default="Defualt")
	article_text = models.TextField()
	article_date = models.DateTimeField(default=datetime.now())
	article_image = models.ImageField(upload_to="images", blank=True)
	article_high_res_image = models.ImageField(upload_to="images", blank=True)

	def __str__(self):
		return self.article_header

	class Meta:
		ordering = ["article_date"]

class Comment(models.Model):
	comment_date = models.DateTimeField(default=datetime.now())
	comment_text = models.TextField()
	commentor_name = models.CharField(max_length=20)
	comment_article = models.ForeignKey(Article, on_delete=models.CASCADE)

	def __str__(self):
		return self.commentor_name

	class Meta:
		ordering = ["comment_date"]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["commentor_name", "comment_text", "comment_date", "comment_article"]

class Subscibe(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	email = models.EmailField()
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["date"]

class SubscibeForm(ModelForm):
	class Meta:
		model = Subscibe
		fields = ["name", "email", "name"]




