from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Genre, Actor, Movie, MovieShots, Rating, RatingStar, Reviews, Direction, Famous_actors, Articles, Info, Series, News, Feed, SalesM


# Register your models here.
# Регистрируем все наши модели в административной панели Django

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  # класс для конфингурации админ панелей
	list_display = ("id", "url", "name")
	list_display_links = ('name',)  # имя ссылки, при нажатии переход на категорию


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ("title", "category", "url", "draft")
	list_filter = ("category", "year") # поле по которому будем фильтровать
	search_fields = ("title", "category__name") # поля по которым будем искать
	list_editable = ("draft",)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
	list_display = ("name", "age", "image", "get_image")
	readonly_fields = ("get_image",)
	def get_image(self, obj): # форма вывода изображений в админке
		return mark_safe(f'<img src={obj.image.url} width="80" height="90" ')

	get_image.description = "Изображение"



admin.site.register(Famous_actors)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Reviews)
admin.site.register(Direction)
admin.site.register(Articles)
admin.site.register(Info)
admin.site.register(Series)
admin.site.register(News)
admin.site.register(Feed)
admin.site.register(SalesM)
# Register your models here.
