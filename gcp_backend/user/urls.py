from django.urls import path
from .views import UserCreation, UserView, ClubAdminView, EmailVarification, ForgetPassword, OauthHelper

urlpatterns = [
    #  {{host}}/user/signup
    path('signup', UserCreation.as_view()),
    path('login', UserView.as_view()),  # method post
    path('logout', UserView.as_view()),  # method delete
    path('profile', UserView.as_view()),  # method get and put for update
    # path('org', OrganisationView.as_view()),
    path('club-admin', ClubAdminView.as_view()),  # method get, post, put
    path('verify/<str:token>', EmailVarification.as_view(), name='verify'),
    path('verifymail', EmailVarification.as_view(), name='verify'),
    path('forgotpass', ForgetPassword.as_view()),
    path('orgtoken/<str:org_id>', OauthHelper.as_view()),
]
