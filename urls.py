from django.urls import path
from . import views

urlpatterns = [
	path('', views.Index),
	path('<int:questions_id>' , views.showchoices, name = 'showchoices'),
	path('<int:questions_id>/result', views.voted, name = 'voted')
]