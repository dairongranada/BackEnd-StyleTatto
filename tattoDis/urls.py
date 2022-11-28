from django.urls import path
from . import views


urlpatterns = [
    path("", views.disponibilidadModelViewCreateList.as_view(), name="disponibilidadModelViewCreateList" ),
    path("<int:pk>/", views.disponibilidadModelUoploadteAndDelete.as_view(), name="disponibilidadModelUoploadteAndDelete"),


]