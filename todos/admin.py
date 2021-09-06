from django.contrib import admin

from todos.models import Project, ToDo

admin.site.register(Project)
admin.site.register(ToDo)
