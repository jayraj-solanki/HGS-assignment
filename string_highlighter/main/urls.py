from django.urls import path
from . import views

urlpatterns = [
    path('highlight_string/', views.highlight_string, name='highlight_string')
]
