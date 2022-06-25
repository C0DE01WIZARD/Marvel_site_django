from django.contrib import admin
from.models import Category, Genre, Actor, Movie, MovieShots, Rating, RatingStar, Reviews, Direction, Famous_actors

# Register your models here.
# Регистрируем все наши модели в административной панели Django


class CategoryAdmin(admin.ModelAdmin): # класс для конфингурации админ панелей
	list_display = ("id", "url", "name")
	list_display_links = ('name',) # имя ссылки


admin.site.register(Famous_actors)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(Direction)
# Register your models here.
