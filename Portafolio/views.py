from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status,generics,mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView,permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import PostPortafolio
from .models import portafolio

from accounts.serializers import CurrentUserTattoSerializer
from django.shortcuts import get_object_or_404


class PortafolioViewCreateList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,):
    serializer_class = PostPortafolio
    queryset = portafolio.objects.all()

    def perform_create(self,serializer):
        user = self.request.user
        serializer.save(idTatuador=user)
        return super().perform_create(serializer)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)





class PortafolioUoploadteAndDelete(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,  mixins.DestroyModelMixin ):
    serializer_class = PostPortafolio
    queryset = portafolio.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)




@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated])
def PortafolioView(request: Request):
    user= request.user 
    serializer = CurrentUserTattoSerializer(instance=user)

    return Response(data= serializer.data, status=status.HTTP_200_OK)




