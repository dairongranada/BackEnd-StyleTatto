from django.urls import path
from quotes import views
from . import views
from .views import *

urlpatterns = [
    path('', views.ViewsQuotes.as_view(), name="quotes"),
    path("<int:pk>/", views.UpdateQuotes.as_view(), name="UpdateQuotes"),
    path("<int:pk>/", views.DeleteQuotes.as_view(), name="DeleteQuotes"),

]
