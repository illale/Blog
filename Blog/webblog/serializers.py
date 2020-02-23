from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ("id", "article_header", "article_text", "article_date", "article_image")
