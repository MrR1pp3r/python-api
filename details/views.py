from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from details.form import FormStudent
from details.models import Student
# Create your views here.


def index(request):
    form = FormStudent(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("stud:result"))

    context = {"form": form}
    return render(request, 'stu/index.html', context)


def result(request):
    form = Student.objects.all()
    return render(request, 'stu/result.html', {"form": form})
