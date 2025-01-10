from django.urls import path
from .views import MemberView, MembershipView

membership_view = MembershipView()

urlpatterns = [
    path('members/', MemberView.as_view(), name='members_view'),
    path('memberships/', membership_view.list_memberships, name='list_memberships'),
    path('memberships/add/', membership_view.add_membership_view, name='add_membership'),
]
