from rest_framework import routers
from django.urls import path , include
from .views import CitasViewsets,PortafolioTatuadoresViewsets,RegistroUsuarioViewsets,RegistroTatuadoresViewsets

router = routers.DefaultRouter()
router.register('agendar citas',CitasViewsets)
router.register('portafolio tatuadores',PortafolioTatuadoresViewsets )
router.register('RegistroTatuadores',RegistroTatuadoresViewsets)
router.register('RegistroUsuario',RegistroUsuarioViewsets)



urlpatterns = [
    path('api/',include(router.urls), name="api")
]