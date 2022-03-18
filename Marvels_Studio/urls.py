from django.urls import path
from .import views

urlpatterns = [  # список
	path('', views.MoviesView.as_view())

]