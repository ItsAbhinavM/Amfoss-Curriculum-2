# todo_list/todo_app/urls.py
from todo_app import views
from django.urls import path , include
from django.contrib import admin

urlpatterns = [ 
    #path('admin/',admin.site.urls),
    #path("",include('todo_app.urls')),
    path('signup/',views.signup,name='signup'),
    path('', views.user_login, name='login'),
    path("home",
        views.ListListView.as_view(), name="index"),
    path("list/<int:list_id>/",
        views.ItemListView.as_view(), name="list"),
    # CRUD patterns for ToDolists
    path("list/add/",views.ListCreate.as_view(),name="list-add"),
    path(
        "list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"
    ),
    # CRUD pattern for ToDoItems
    path(
        "list/<int:list_id>/item/add/",
        views.ItemCreate.as_view(),
        name="item-add",
    ),
    #Used for the checkbox
    path(
        "list/<int:list_id>/item/<int:pk>/",
        views.ItemUpdate.as_view(),
        name="item-update"
    ),
    # this may be used_
    #path('todo/<int:pk>/update/', ItemUpdate.as_view(), name='item_update'),path('todo/', todo_list, name='todo_list'),
    path(
        "list/<int:list_id>/item/<int:pk>/delete/",
        views.ItemDelete.as_view(),
        name="item-delete",
    ),
    path("logout",views.logout.as_view(),name='logout'),
]