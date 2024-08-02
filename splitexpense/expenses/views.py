# expenses/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Expense
from .forms import ExpenseForm
from django.urls import reverse_lazy

class ExpenseListView(ListView):
    model = Expense
    template_name = 'expenses/expense_list.html'

class ExpenseDetailView(DetailView):
    model = Expense
    template_name = 'expenses/expense_detail.html'

class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/expense_form.html'
    success_url = reverse_lazy('expense_list')

class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/expense_form.html'
    success_url = reverse_lazy('expense_list')

class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'expenses/expense_confirm_delete.html'
    success_url = reverse_lazy('expense_list')
