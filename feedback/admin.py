from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Feedback

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}), 
    )

admin.site.register(Feedback)
