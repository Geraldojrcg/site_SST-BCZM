from django.urls import path
from . import views

app_name = 'hotsite'

urlpatterns = [
    path('', views.hotsite, name='hotsite'),
]