from django.shortcuts import render
from .models import Article
from rest_framework import viewsets
from .serializers import ArticleSerializer
# Create your views here.

class ArticleView(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

def home(request):
	articles = Article.objects.order_by("-article_date")
	context = {
		'article1': articles[0],
		'article2': articles[1],
		'article3': articles[2],
		'article4': articles[3],
		'article5': articles[4],
		'article6': articles[5],
		'article7': articles[6],
		'article8': articles[7],
		'article9': articles[8],
	}
	return render(request, 'webblog/home.html', context)
