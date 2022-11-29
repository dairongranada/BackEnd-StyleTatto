from rest_framework import status,generics,mixins
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import render, get_object_or_404

from .serializer import *
from .models import *



# Create your views here.

#-------------------------------------------------------------------------------------------#
#-----------------------API CITAS METHODS GET POST PUT DELETE-------------------------------#
#-------------------------------------------------------------------------------------------#



class ViewsQuotes(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,):
    serializer_class = RegisterQuotes
    queryset = Quotes.objects.all()
    
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class DeleteQuotes(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,):
    serializer_class = RegisterQuotes
    queryset = Quotes.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class UpdateQuotes(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    serializer_class = UpdateQuotes
    queryset = Quotes.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)





# class DeleteQuotes(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     serializer_class = RegisterQuotes
#     queryset = Quotes.objects.all()

#     def get(self, request: Request, id):

#         quote = Quotes.objects.filter(id_quotes= id).first()

#         if quote == None :
#             request = {
#             "response":"cita no encontrada"
#             }

#             return Response (data=request, status=status.HTTP_404_NOT_FOUND)

#         request = {
#             "response":"cita encontrada",
#             "quotes" : {
#                 "id_quote": quote.id_quotes,
#                 "date" : quote.date,
#                 "time" : quote.time,
#                 "img" : quote.img,
#                 "description" : quote.description,
#                 "user" : quote.userID.__str__(),
#                 "artist_tatoo": quote.artist_tattoo.__str__(),
#                 "isActive" : quote.isActive
#             }
#         }
#         return Response(data=request, status=status.HTTP_200_OK)
        

#     def delete(self,request:Request, id):

#         print(request.data)

#         quote = Quotes.objects.filter(id_quotes= id).first()
#         if quote == None :

#             request = {
#             "response":"cita no encontrada"
#             }
#             return Response (data=request, status=status.HTTP_404_NOT_FOUND)

#         quote.delete()

#         request = {
#             "response":"cita eliminada exitosamente"
#         }

#         return Response (data=request, status=status.HTTP_200_OK)


#     def delete(self, request: Request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class ViewsQuotes(generics.GenericAPIView):
#     permission_classes = []
#     serializer_class = RegisterQuotes

#     def post(self, request:Request):
#         data = request.data
#         serializer = self.serializer_class(data=data)


#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "massage":"cita registrada",
#                 "data" : serializer.data
#             }

#             return Response (data=response, status= status.HTTP_201_CREATED)

#         return Response (data=serializer.errors, status= status.HTTP_201_CREATED)