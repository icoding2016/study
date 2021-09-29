from django.contrib import admin

# Register your models here.
from todo_app.models import ToDo

admin.site.register(ToDo)
