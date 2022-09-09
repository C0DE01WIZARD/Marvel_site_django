from django import forms  # импортируем для создания классов формы
from .models import *  # импортируем все модели


class Review(forms.ModelForm):
	"Форма отзывов"

	class Meta:
		model = Reviews
		fields = ("name", "email", "text")


class FormAdd(forms.Form):  # класс формы который будет представлять на странице "+"
	# наследуется от базового класса Forms
	# форму добавляем в views.py в  переменную form
	title = forms.CharField(max_length=255, label='Название')
	tagline = forms.CharField(max_length=100, label='Слоган')
	slug = forms.SlugField(max_length=255, label="URL")
	is_published = forms.BooleanField(label='Публикация', required=False)  # required=False-не обязательное поле
	cat = forms.ModelChoiceField(queryset=Movie.objects.all(), label='Категория')
