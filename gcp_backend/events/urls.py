from django.urls import path
from .views import EventCreation, SubscriptionCreation, TagView, Filter, TypeView

urlpatterns = [
    path('create', EventCreation.as_view()),
    path('edit', EventCreation.as_view()),
    path('',Filter.as_view()),
    path('subs', SubscriptionCreation.as_view()),
    path('tags', TagView.as_view()),
    path('type', TypeView.as_view())
]