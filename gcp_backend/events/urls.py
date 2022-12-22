from django.urls import path
from .views import EventCreation, SubscriptionCreation, TagView, Filter

urlpatterns = [
    path('create/', EventCreation.as_view()),
    path('edit', EventCreation.as_view()),
    path('org_id=<int:org_id>',Filter.as_view()),
    path('subs', SubscriptionCreation.as_view()),
    path('tags', TagView.as_view())
]