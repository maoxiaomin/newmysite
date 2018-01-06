from django.contrib import admin
from . import models

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'gender', 'email', 'mobile', 'is_superuser', 'is_active')
    list_filter = ('gender', 'is_superuser', 'date_joined', 'is_superuser','is_active')
    search_fields = ('username', 'email', 'mobile')

admin.site.register(models.UserProfile, UserProfileAdmin)