from django.contrib import admin
from view_api.models import APIInfo

# Register your models here.


class APIInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(APIInfo, APIInfoAdmin)
