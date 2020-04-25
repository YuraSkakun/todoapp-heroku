from django.contrib import admin

# Register your models here.

from tasks.models import TodoItem

# admin.site.register(TodoItem)

@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
	list_display = ('description', 'is_completed', 'created')
	