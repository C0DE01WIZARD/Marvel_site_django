from django import forms
from.models import Reviews, Rating, RatingStar


class Review(forms.ModelForm):
	"Форма отзывов"
	class Meta:
		model = Reviews
		fields = ("name", "email", "text")

