from django.urls import path
from . import views
from django.views.decorators.cache import cache_page  # импорт кэша

from Marvels_Studio.views import *

urlpatterns = [  # список url

	path('search/', SearchResult.as_view(), name='search' ), # поиск по сайту

	path('pay/', Pay.as_view(), name='pay'),

	path('news/', views.Newss, name='news'),  #
	# path('', cache_page(60) (About), name='about'),

	path('', About, name='about'),
	path('auth/', Auth.as_view(), name='auth'),
	path('logout/', logout_user, name='logout'),

	path('message/', Message, name='message'),

	path('series/', SeriesD.as_view(), name='series'),
	path('series/<slug:slug>/', SeriesDet.as_view(), name='seriesdet'),

	path('actors/', Actors, name='actor'),
	path('actors/<slug:slug>/', ActorsDet.as_view(), name='actors'),

	path('movie/', Movies, name='movies'),
	path('movie/<slug:slug>/', MovieDet.as_view(), name='movie'),

	path('trailers/', Trailer.as_view(), name='trailers'),
	path('about_us/', views.AboutUsView.as_view(), name="about_us"),
	path('reg/', Register.as_view(template_name="movies/reg.html"), name='reg'),

	path('list/', Sales, name='sales'),

	path('add/', views.add, name='add'),
	path('feed/', FeedAdd, name='feed'),
]
