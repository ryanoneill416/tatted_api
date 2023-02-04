from django.urls import path
from users import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
]