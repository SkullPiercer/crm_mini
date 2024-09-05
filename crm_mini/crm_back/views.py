from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from .forms import GroupForm, StudentCreateForm, StudentUpdateForm
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


def group_detail(request, id):
    template = 'group_detail.html'
    group = get_object_or_404(Group, id=id)

    if request.method == 'POST':
        form = StudentCreateForm(request.POST, group=group)
        if form.is_valid():
            name_instance = form.save(commit=False)
            name_instance.group = group
            name_instance.save()
    else:
        form = StudentCreateForm(group=group)

    all_students = Student.objects.filter(group=group)

    return render(request, template, context={'group': group, 'form': form, 'all_students':all_students})


def student_detail(request, id):
    template = 'student_detail.html'
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = StudentUpdateForm(instance=student)
    return render(request, template, context={'student':student, 'form': form})


def download_data(request):
    template = 'download_page.html'
    return render(request, template)

def students_list(request):
    template = 'students_list.html'
    name = request.GET.get('name')
    if name:
        students = Student.objects.filter(name__icontains=name)
    else:
        students = Student.objects.all()
    return render(request, template, context={'students':students})
