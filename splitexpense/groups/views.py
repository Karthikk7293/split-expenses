# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Groups, GroupMember
from .forms import GroupsForm, GroupMemberForm
from django.urls import reverse_lazy

# List view for groups
class GroupsListView(ListView):
    model = Groups
    template_name = 'groups/main_table_list.html'

# Detail view for a specific group
class GroupsDetailView(DetailView):
    model = Groups
    template_name = 'groups/main_table_detail.html'

# Create view for a new group
class GroupsCreateView(CreateView):
    model = Groups
    form_class = GroupsForm
    template_name = 'groups/main_table_form.html'
    success_url = reverse_lazy('main_table_list')

# Update view for an existing group
class GroupsUpdateView(UpdateView):
    model = Groups
    form_class = GroupsForm
    template_name = 'groups/main_table_form.html'
    success_url = reverse_lazy('main_table_list')

# Delete view for a group
class GroupsDeleteView(DeleteView):
    model = Groups
    template_name = 'groups/main_table_confirm_delete.html'
    success_url = reverse_lazy('main_table_list')

# Create view for adding a group member
class GroupMemberCreateView(CreateView):
    model = GroupMember
    form_class = GroupMemberForm
    template_name = 'groups/group_member_form.html'

    def form_valid(self, form):
        form.instance.main_table_uid = get_object_or_404(Groups, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('groups/main_table_detail', kwargs={'pk': self.kwargs['pk']})
