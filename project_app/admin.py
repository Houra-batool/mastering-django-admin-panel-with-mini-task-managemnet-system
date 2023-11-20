from django.contrib import admin
from project_app.models import Project, Task, Category


admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Task)
