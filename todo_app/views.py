#from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .forms import SignUpForm , LoginForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ToDoList , ToDoItem
from django.urls import reverse , reverse_lazy

from django.shortcuts import render,redirect
from django.contrib.auth import login ,authenticate
from django.contrib.auth.forms import UserCreationForm

# for  the login page : 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'todo_app/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'todo_app/login.html', {'form': form})


'''class signup(LoginView):

    template_name='todo_app/signup.html'
    fields="__all__"
    def get_success_url(self):
        return reverse_lazy("todo_app/todo_list.html")
class login(LoginView):
    template_name='todo_app/login.html'
    fields="__all__"
    def get_success_url(self):
        return reverse_lazy("todo_app/todo_list.html")
'''
class ListListView(LoginRequiredMixin,ListView):
    model=ToDoList
    template_name="todo_app/index.html"
    
class ItemListView(LoginRequiredMixin,ListView):
    model=ToDoItem
    template_name="todo_app/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])
    
    def get_context_data(self):
        context=super().get_context_data()
        context["todo_list"]=ToDoList.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(LoginRequiredMixin,CreateView):
    model=ToDoList
    fields=["title"]
    template_name="todo_app/todolist_form.html"

    def get_context_data(self):
        context=super().get_context_data()
        context["title"]=" Add a new list"
        return context

class ItemCreate(LoginRequiredMixin,CreateView):
    model=ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date"
    ]

    def get_intitial(self):
        initial_data=super(ItemCreate,self).get_initial()
        todo_list=ToDoList.objects.get(id=self.kwargs["List_id"])
        initial_data[todo_list]=todo_list
        return initial_data
    
    def get_context_data(self):
        context=super(ItemCreate,self).get_context_data()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"]=todo_list
        context["title"]="Create a new item"
        return context
    
    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ItemUpdate(LoginRequiredMixin,UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
        "completed"
    ]

    #form_class=ToDoItemForm
    template_name= 'todo_app/itemupdate.html'
    success_url = reverse_lazy('todo_list')

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context
    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])
    
class ListDelete(LoginRequiredMixin,DeleteView):
    model=ToDoList
    success_url=reverse_lazy("index")

class ItemDelete(LoginRequiredMixin,DeleteView):
    model=ToDoItem

    def get_success_url(self):
        return reverse_lazy("list",args=[self.kwargs["list_id"]])
        
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["todo_list"]=self.object.todo_list
        return context
    
class logout(LogoutView):
    template_name="todo_app/logout.html"