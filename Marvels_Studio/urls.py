from django.urls import path
from . import views

urlpatterns = [  # список url
	path('', views.MoviesView.as_view()),  # пустая так как главная страница
	#path('<slug:slug>/', views.Detail.as_view()),  # принимаем pk как число int
	path('<int:pk>/', views.Detail.as_view()),  # принимаем pk как число int
	path('base/', views.base.as_view(), name='base'),
	path('reg/', views.reg, name='reg')
]
