from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_form, name='submit_form'),
    path('results/<str:name>/<str:email>/', views.index, name='index'),
]
