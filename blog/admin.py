from django.contrib import admin
from.models import custom_user,comment,post
# Register your models here.
admin.site.register(custom_user)
admin.site.register(comment)
admin.site.register(post)