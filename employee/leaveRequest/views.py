from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from leaveRequest.models import LeaveRequest
from leaveRequest.serializers import LeaveRequestSerializer
# class LeaveRequestView()
class ListCreateLeaveRequestView(ListCreateAPIView):
    model = LeaveRequest
    serializer_class = LeaveRequestSerializer
    def get_queryset(self):
        return LeaveRequest.objects.all()
    def create(self, request, *args, **kwargs):
        serializer = LeaveRequestSerializer(data=request.data) #get data from body
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'message': 'Create a new LeaveRequest successful!'
            }, status=status.HTTP_201_CREATED)
        return JsonResponse({
            'message': 'Create a new LeaveRequest unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
