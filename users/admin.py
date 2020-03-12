from django.contrib import admin

# Register your models here.
from .models import Profile
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username','image','date_joined']

    fieldsets = UserAdmin.fieldsets + (
            ('Profile', {'fields': ('image',)}),
    )

#admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)