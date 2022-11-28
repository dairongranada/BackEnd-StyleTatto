from django.urls import path
from . import views


urlpatterns = [
    path("", views.ProfileTCreateList.as_view(), name="ProfileTCreateList" ),
    path("<int:pk>/", views.ProfileTUoploadteAndDelete.as_view(), name="ProfileTUoploadteAndDelete"),
    path("perfilProfesional/", views.perfilProfesional, name="perfilProfesional"),


]