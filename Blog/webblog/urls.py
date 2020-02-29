from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('articles', views.ArticleView)

urlpatterns = [
	path('', views.home, name="home"),
	path('rest', include(router.urls)),
	path('articles/<int:pk>', views.ArticleDetail.as_view()),
	path('comments', views.CommentList.as_view()),
	path('comments/<int:pk>', views.CommentDetail.as_view())
]
