from django.urls import path
from . import views
from .views import Payment
from.views import *

urlpatterns=[
	path('payment/',Payment.as_view(), name = 'Payment')

	]