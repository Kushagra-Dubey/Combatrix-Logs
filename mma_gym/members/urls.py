from django.urls import path
from .views import list_members, add_member_view, update_member_view, delete_member_view

app_name = 'members' 

urlpatterns = [
    path("members/", list_members, name="list-members"),
    path("members/add/", add_member_view, name="add-member"),
    path("members/update/", update_member_view, name="update-member"),
    path("members/delete/", delete_member_view, name="delete-member"),
]
