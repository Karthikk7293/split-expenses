# expenses/forms.py

from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'description', 'image', 'expense_members', 'paid_by', 'group']
