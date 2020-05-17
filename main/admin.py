from django.contrib import admin
from .models import project, Message

admin.site.register(project)
admin.site.register(Message)