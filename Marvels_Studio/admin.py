from django.contrib import admin
from.models import Category, Genre, Actor, Movie, MovieShots, Rating, RatingStar, Reviews, Direction

# Register your models here.
# Регистрируем все наши модели в административной панели Django
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(Direction)
# Register your models here.
