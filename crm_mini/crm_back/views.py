from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .forms import GroupForm
from .models import Group, Student


def home(request):
    template = 'home.html'
    return render(request, template)


def group_list(request):
    template = 'group_list.html'
    groups = Group.objects.all()
    return render(request, template, context={'groups': groups})


def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(reverse_lazy('back:group_list'))
    else:
        form = GroupForm()
    return render(request, 'create_group.html', {'form': form})
