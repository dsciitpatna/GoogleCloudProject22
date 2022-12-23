from django.urls import path
from .views import UserCreation, OrganisationView, UserView

urlpatterns = [
    path('signup', UserCreation.as_view()),
    path('login', UserView.as_view()),
    path('login/refresh/', UserView.as_view()),
    path('user_id=<int:user_id>', UserView.as_view()),
    path('profile', UserView.as_view()),
    path('org/', OrganisationView.as_view())
]