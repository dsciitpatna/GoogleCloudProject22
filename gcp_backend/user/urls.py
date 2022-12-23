from django.urls import path
from .views import UserCreation, OrganisationView, Userinfo

urlpatterns = [
    path('signin', UserCreation.as_view()),
    path('login/', UserCreation.as_view()),
    path('info/user=<int:user_id>', Userinfo.as_view()),
    path('login/refresh/', UserCreation.as_view()),
    path('<int:user_id>', UserCreation.as_view()),
    path('org/', OrganisationView.as_view())
]