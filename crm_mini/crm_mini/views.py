from django.shortcuts import render

from .models import Group, Student


def home(request):
    template = 'home.html'
    return render(request, template)


def create_group(request):
    template = 'create_group.html'
    return render(request, template)

def group_list(request):
    template = 'group_list.html'
    groups = Group.objects.all()
    return render(request, template, context={'groups': groups})