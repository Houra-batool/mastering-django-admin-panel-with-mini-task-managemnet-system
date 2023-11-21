from django.contrib import admin
from project_app.models import Project, Task, Category

admin.site.site_header = 'XYZ Task Management'
admin.site.index_title = 'Welcome to XYZ Task Management'


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'project', 'assigned_to_list')
    list_editable = ('status',)
    list_filter = ('status', 'project__name', 'due_date')
    search_fields = ('title', 'description', 'assigned_to__username')
    date_hierarchy = 'due_date'
    actions = ['mark_as_pending']
    save_as = True
    save_on_top = True
    raw_id_fields = ("project",)

    def assigned_to_list(self, obj):
        return ", ".join([user.username for user in obj.assigned_to.all()])

    assigned_to_list.short_description = 'Assigned To'

    def mark_as_pending(self, request, queryset):
        queryset.update(status='PENDING')

    mark_as_pending.short_description = "Mark selected tasks as pending"


admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Task, TaskAdmin)
