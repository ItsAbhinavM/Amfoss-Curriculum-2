# todo_list/todo_app/models.py
from django.utils import timezone

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)
    #The timedelta function is used to give the differences in date and time
    #The time.now returns the current date and time as a naive datetime (getting the current date and time.)

class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)
    #The model define the strucure of stored data, including the field types and possibly also their maximum size .
    #In Django, you'd create a Model that defines what information you want to store. Each piece of information (like name, age, email) is called a "field." 
    #CharField is used for strong text


    def get_absolute_url(self):
        #self represents an instance of class .
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title #prints the first alphabet of every letter from self

class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    completed=models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"] 