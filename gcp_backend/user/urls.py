from django.urls import path
from .views import UserCreation

urlpatterns = [
    path('signin/', UserCreation.as_view()),
    path('login/', UserCreation.as_view()),
    path('login/refresh/', UserCreation.as_view()),
    path('user_id=<int:user_id>', UserCreation.as_view())
]