from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('articles', views.ArticleView)

urlpatterns = [
	path('articles/', views.home, name="home"),
	path('rest', include(router.urls)),
	path('articles/<int:pk>', views.ArticleDetail.as_view()),
	path('comments', views.CommentList.as_view()),
	path('comments/<int:pk>', views.CommentDetail.as_view()),
	path('comments/list/<int:pk>', views.ArticleComments.as_view()),
	path('comments/create', views.saveform, name="saveform"),
	path('', views.front, name="frontpage"),
	path('subscribe', views.saveEmail, name="subscribe"),
	path('recent_article', views.MostRecentArticle.as_view()),
]
