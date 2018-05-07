from django.contrib import admin

# Register your models here.

from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','modified_time','category']

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
