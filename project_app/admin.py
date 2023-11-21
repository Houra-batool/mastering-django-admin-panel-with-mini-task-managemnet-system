from django.contrib import admin
from project_app.models import Project, Task, Category


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'project', 'assigned_to_list')
    list_editable = ('status',)
    list_filter = ('status', 'project__name', 'due_date')
    search_fields = ('title', 'description', 'assigned_to__username')
    date_hierarchy = 'due_date'

    def assigned_to_list(self, obj):
        return ", ".join([user.username for user in obj.assigned_to.all()])

    assigned_to_list.short_description = 'Assigned To'



admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Task, TaskAdmin)
