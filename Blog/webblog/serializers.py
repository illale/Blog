from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ("id", "article_header", "article_text", "article_date", "article_image")

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ("id", "comment_date", "comment_text", "commentor_name", "comment_article")