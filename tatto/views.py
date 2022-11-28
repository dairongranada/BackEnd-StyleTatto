from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status,generics,mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import PostArtist
from .models import Tattoo_artist

from accounts.serializers import CurrentUserTattoSerializer
from django.shortcuts import get_object_or_404


class ProfileTCreateList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PostArtist
    queryset = Tattoo_artist.objects.all()

    def perform_create(self,serializer):
        user = self.request.user
        serializer.save(artist=user)
        return super().perform_create(serializer)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)





class ProfileTUoploadteAndDelete(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,):


    serializer_class = PostArtist
    queryset = Tattoo_artist.objects.all()


    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    






@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
def perfilProfesional(request: Request):

    user= request.user 

    serializer = CurrentUserTattoSerializer(instance=user)

    return Response(data= serializer.data, status=status.HTTP_200_OK)




