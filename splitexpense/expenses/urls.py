# expenses/urls.py

from django.urls import path
from .views import (
    ExpenseListView,
    ExpenseDetailView,
    ExpenseCreateView,
    ExpenseUpdateView,
    ExpenseDeleteView
)

urlpatterns = [
    path('', ExpenseListView.as_view(), name='expense_list'),
    path('expense/<uuid:pk>/', ExpenseDetailView.as_view(), name='expense_detail'),
    path('expense/create/', ExpenseCreateView.as_view(), name='expense_create'),
    path('expense/<uuid:pk>/update/', ExpenseUpdateView.as_view(), name='expense_update'),
    path('expense/<uuid:pk>/delete/', ExpenseDeleteView.as_view(), name='expense_delete'),
]
