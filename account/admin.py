from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.modelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']

admin.site.register(Profile, ProfileAdmin)