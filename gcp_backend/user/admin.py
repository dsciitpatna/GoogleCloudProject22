from django.contrib import admin
from .models import Organization, User
# Register your models here.
# admin.site.register(Organization)
admin.site.register(User)


@admin.register(Organization)
class OrgAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'is_active', )
    # search_fields = ('name')