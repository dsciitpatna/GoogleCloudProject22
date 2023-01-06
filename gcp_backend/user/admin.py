from django.contrib import admin
from .models import Organization, User
# Register your models here.
admin.site.register(Organization)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    @admin.action(description='Lock Selected User')
    def lock_user(self, request, queryset):
        queryset.update(is_locked=True)
        self.message_user(request, "Selected User Locked")


    list_display = ( 'userid','name', 'email','role', 'organization_id')
    actions = [lock_user]
    list_filter = ('role', 'is_locked')
    fieldsets = (
        ('Basic Information', {
            'fields': (
                'name',
                'email',
                'phone_number',
                'role'
                )
        }),
        ('Internal Flags', {
            'fields': (('is_active', 'is_locked'), 'password')
        })
    )
    empty_value_display = '-empty-'
    search_fields = ['name', 'userid', 'email', 'phone_number', 'organization_id']

    