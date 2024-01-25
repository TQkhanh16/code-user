from django.urls import path
from leaveRequest import views

urlpatterns = [
    path('leaveRequest', views.ListCreateLeaveRequestView.as_view()),
    # path('leaveRequest/<int:pk>', views.UpdateDeleteLeaveRequestView.as_view()),
    # path('leaveRequest/',)
]