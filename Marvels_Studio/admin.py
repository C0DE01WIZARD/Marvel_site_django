from django.contrib import admin
from.models import Category, Genre, Actor, Movie, MovieShots, Rating, RatingStar, Reviews, Direction, Famous_actors, Articles

# Register your models here.
# Регистрируем все наши модели в административной панели Django



class CategoryAdmin(admin.ModelAdmin): # класс для конфингурации админ панелей
	list_display = ("id", "url", "name")
	list_display_links = ('name',) # имя ссылки


class CatAdmin(admin.ModelAdmin): # класс для конфингурации админ панелей
	list_display2 = ("id", "url")
	list_display_links2 = ('poster') # имя ссылки

admin.site.register(Famous_actors)
admin.site.register(Category, CategoryAdmin) # регистрируем нашу нашу модель
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Movie, CatAdmin)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(Direction)
admin.site.register(Articles)
# Register your models here.
