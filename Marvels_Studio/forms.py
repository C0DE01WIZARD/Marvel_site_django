from django import forms  # импортируем для создания классов формы
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import *  # импортируем все модели


class Review(forms.ModelForm):
	"Форма отзывов"

	class Meta:
		model = Reviews
		fields = ("name", "email", "text")


class FormAdd(forms.Form):  # класс формы который будет представлять на странице "добавить фильма"
	# наследуется от базового класса Forms
	# форму добавляем в views.py в  переменную form
	title = forms.CharField(max_length=255, label='Название') # атрибуты для отображения формы
	tagline = forms.CharField(max_length=100, label='Слоган')
	slug = forms.SlugField(max_length=255, label="URL")
	is_published = forms.BooleanField(label='Публикация', required=False)  # required=False-не обязательное поле
	cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label="Катеория не выбрана") # выпадающий список для выбора категорий


class RegisterForm(UserCreationForm): # форма регистрации
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
	email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
	password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
	password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class LoginUserForm(AuthenticationForm):
	username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': "form-input"}))