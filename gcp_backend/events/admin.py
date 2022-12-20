from django.contrib import admin
from .models import Event, Type, Tag, Subscription
# Register your models here.

admin.site.register(Event)
admin.site.register(Type)
admin.site.register(Tag)
admin.site.register(Subscription)