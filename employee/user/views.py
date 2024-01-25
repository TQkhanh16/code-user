from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from user.models import User
from user.serializers import UserSerializer
# class UserView()
class ListCreateUserView(ListCreateAPIView):
    model = User
    serializer_class = UserSerializer
    def get_queryset(self):
        return User.objects.all()
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data) #get data from body
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new User successful!'
            }, status=status.HTTP_201_CREATED)
        return JsonResponse({
            'message': 'Create a new User unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)
# class UpdateDeleteCarView(RetrieveUpdateDestroyAPIView):
    # model = Car
    # serializer_class = CarSerializer
    # def put(self, request, *args, **kwargs):
    #     car = get_object_or_404(Car, id=kwargs.get('pk'))
    #     serializer = CarSerializer(post, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse({
    #             'message': 'Update Car successful!'
    #         }, status=status.HTTP_200_OK)
    #     return JsonResponse({
    #         'message': 'Update Car unsuccessful!'
    #     }, status=status.HTTP_400_BAD_REQUEST)
    # def delete(self, request, *args, **kwargs):
    #     car = get_object_or_404(Car, id=kwargs.get('pk'))
    #     car.delete()
    #     return JsonResponse({
    #         'message': 'Delete Car successful!'
    #     }, status=status.HTTP_200_OK)