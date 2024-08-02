# urls.py

from django.urls import path
from .views import (
    GroupsListView,
    GroupsDetailView,
    GroupsCreateView,
    GroupsUpdateView,
    GroupsDeleteView,
    GroupMemberCreateView
)

urlpatterns = [
    path('', GroupsListView.as_view(), name='main_table_list'),
    path('group/<uuid:pk>/', GroupsDetailView.as_view(), name='main_table_detail'),
    path('group/create/', GroupsCreateView.as_view(), name='main_table_create'),
    path('group/<uuid:pk>/update/', GroupsUpdateView.as_view(), name='main_table_update'),
    path('group/<uuid:pk>/delete/', GroupsDeleteView.as_view(), name='main_table_delete'),
    path('group/<uuid:pk>/add-member/', GroupMemberCreateView.as_view(), name='group_member_create'),
]
