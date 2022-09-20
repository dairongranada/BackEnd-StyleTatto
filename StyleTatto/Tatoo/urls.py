from rest_framework import routers
from django.urls import path , include
from .views import  *

router = routers.DefaultRouter()
router.register('RegistroTatuadores',RegistroTatuadoresViewsets)
router.register('RegistroUsuario',RegistroUsuarioViewsets)
router.register('Registro Departamentos',RegistroDepartamentosViewsets)
router.register('Registro Localidades',RegistroLocalidadesViewsets)
router.register('agendar citas',CitasViewsets)
router.register('portafolio tatuadores',PortafolioTatuadoresViewsets )


urlpatterns = [
    path('api/',include(router.urls), name="api")
]