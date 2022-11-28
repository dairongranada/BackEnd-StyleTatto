from django.urls import path
from . import views


urlpatterns = [
    path("", views.PortafolioViewCreateList.as_view(), name="PortafolioViewCreateList" ),
    path("<int:pk>/", views.PortafolioUoploadteAndDelete.as_view(), name="PortafolioUoploadteAndDelete"),
    path("Portafolio/", views.PortafolioView, name="Portafolio"),


]