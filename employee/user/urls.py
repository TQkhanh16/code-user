from django.urls import path
from user import views

urlpatterns = [
    path('user', views.ListCreateUserView.as_view()),
    path('user/<int:pk>', views.UpdateDeleteUserView.as_view()),
    # path('users/',)
]