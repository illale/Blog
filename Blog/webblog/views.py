from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article, Comment, CommentForm
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework.permissions import AllowAny
# Create your views here.

class ArticleView(viewsets.ModelViewSet):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class CommentList(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

class ArticleComments(generics.ListAPIView):
	serializer_class = CommentSerializer

	def get_queryset(self):
		number = self.kwargs["pk"]
		print(number)
		return Comment.objects.filter(comment_article=number)

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
		'form': CommentForm(),
	}
	return render(request, 'webblog/home.html', context)

def saveform(request):
	form = CommentForm(request.POST or None)
	if form.is_valid():
		form.save()

	return HttpResponseRedirect('http://127.0.0.1:8000/home/')


