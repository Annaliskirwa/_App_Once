from django.contrib import admin
from .models import Editor,tags

admin.site.register(Editor)
# admin.site.register(Article)
admin.site.register(tags)
