from django.urls import path
from .views import UserCreation, OrganisationView, UserView

urlpatterns = [
    path('signup', UserCreation.as_view()),
    path('login', UserView.as_view()), # method post
    path('logout', UserView.as_view()), # method delete
    path('profile', UserView.as_view()), # method get and put for update
    path('org/', OrganisationView.as_view())
]