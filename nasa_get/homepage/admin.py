from django.contrib import admin
from homepage.models import UserAPIs

# Register your models here.


class UserAPIsAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserAPIs, UserAPIsAdmin)
