from . import views
from django.urls import path,include
from .views import ChangePasswordView,AllviewP
from rest_framework import routers


router = routers.DefaultRouter()
router.register("TattoList",AllviewP )


urlpatterns = [
     path("signup/", views.signUpView.as_view(), name="signup" ),
     path("login/", views.Login.as_view(),name="login"),
     path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
     path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
     path("api/getUsers/",views.UserRetrieveAPIView.as_view(),name='getUsers' ),
     path("allUsers/", views.ProfileTCreateList.as_view(), name="ProfileTCreateList" ),
     path("allUsers/<int:pk>/", views.userUpdate.as_view(), name="userUpdate" ),

     path("listTattoo/", include(router.urls))


]