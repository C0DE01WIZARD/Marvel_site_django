
from django.db import models
from datetime import date

# Create your models here.

# пишем модели

class Category(models.Model): # импортируем models из django.db наследуются от класса Model
	name = models.CharField("Категория", max_length=150)
	description = models.TextField('Описание', max_length=300)
	url = models.SlugField(max_length=150, unique=True) # unique - уникальное

# метод __str__ для возвращения строкового представления модели
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

# работающий класс


class Actor(models.Model):
	name = models.CharField('Имена актёров', max_length=150)
	age = models.PositiveSmallIntegerField('Возраст актёров', default=0)
	description = models.TextField('Описание', max_length=1500)
	image = models.ImageField('Фотография актёра', upload_to='actor/', default='default title')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Актёр"
		verbose_name_plural = "Актёры"
# работающий класс


class Direction(models.Model):
	name = models.CharField('Имена режиссёров', max_length=150)
	age = models.PositiveSmallIntegerField('Возраст режиссёров', default=0)
	description = models.TextField('Описание', max_length=1500)
	image = models.ImageField('Фотография режиссёра', upload_to='direction/')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Режисёры"
		verbose_name_plural = "Режисёры"

# работающий класс


class Genre(models.Model):
	name = models.CharField('Наименование жанра', max_length=150)
	description = models.TextField('Описание', max_length=150, default='')
	url = models.SlugField(max_length=150, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Жанр"
		verbose_name_plural = "Жанры"

# работающий класс


class Movie(models.Model):
	title = models.CharField("Название", max_length=100)
	tagline = models.CharField("Слоган", max_length=100, default='')
	description = models.TextField("Описание")
	#poster = models.ImageField('Постер', upload_to='poster/', default='default title')
	year = models.PositiveSmallIntegerField('Дата выхода', default=2008)
	country = models.CharField('Страна', max_length=30)
	# создаем связь многие ко многим ManyToManyField
	# help_text - для дополнительного отображения виджете формы
	direction = models.ManyToManyField(Direction, verbose_name='режиссёр', related_name='film_direction')
	# related_name-родственное имя
	actors = models.ManyToManyField(Actor, verbose_name='актёры', related_name='film_actor')
	genres = models.ManyToManyField(Genre, verbose_name='жанры')
	world_premier = models.DateField('Премьера в мире', default=date.today)
	budget = models.PositiveSmallIntegerField('Бюджет', default=0, help_text='указать сумму в долларах')
	fees_in_usa = models.PositiveSmallIntegerField(
		'Сборы в США', default=0, help_text='указывать сумму в долларах'
	)
	fees_in_world = models.PositiveSmallIntegerField(
		'Сборы в мире', default=0, help_text='указывать в долларах'
	)

	category = models.ForeignKey( # Foreign - отношение Многие к одному
		# указываем модель катергории Category, обязательный аргумент on_delete=models.SET_NULL
		# SET_NULL указывает что при удалении поле будет равно нулю
		Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True
	)

	url = models.SlugField(max_length=130, unique=True)
	# draft - черновик
	draft = models.BooleanField('Черновик', default=False)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Фильм'
		verbose_name_plural = 'Фильмы'

# кадры из фильма


class MovieShots(models.Model):
	title = models.CharField('Заголовок', max_length=100)
	description = models.TextField('Описание')
	image = models.ImageField('Изображение', upload_to='movie_shots/')
	movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)
	# CASCADE - при удалении всех фильмов кадры удаляться

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Кадр из фильма'
		verbose_name_plural = 'Кадры из фильма'
# звёзды рейтинга


class RatingStar(models.Model):
	value = models.SmallIntegerField('Значение,', default=0)

	def __str__(self):
		return self.value

	class Meta:
		verbose_name = 'Звёзда рейтинга'
		verbose_name_plural = 'Звёзды рейтинга'

# Рейтинг


class Rating(models.Model):
	ip = models.CharField('IP адрес', max_length=15)
	star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='звёзда')
	movie = models.ForeignKey(Movie, on_delete=models.CharField, verbose_name='фильм')

	def __str__(self):
		return f"{self.star} - {self.movie}"

	class Meta:
		verbose_name = 'Рейтинг'
		verbose_name_plural = 'Рейтинги'


# Отзывы
class Reviews(models.Model):

	email = models.EmailField()
	name = models.CharField('Имя', max_length=100)
	text = models.CharField('Сообщение', max_length=5000)
	parent = models.ForeignKey(
		'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
	)
	movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} - {self.movie}"

	class Meta:
		verbose_name = 'Отзыв'
		verbose_name_plural = 'Отзывы'
# Create your models here.
