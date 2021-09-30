from django.db import models

# Create your models here.
class ToDo(models.Model):
    task = models.CharField(max_length=1000)
    create_time = models.DateTimeField(auto_now_add=True)
    handle_time = models.DateTimeField()

    def __str__(self) -> str:
        return f"Task:{self.task}, time:{self.handle_time}, created:{self.create_time}"
