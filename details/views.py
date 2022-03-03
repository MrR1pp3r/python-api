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
    form = Student.objects.order_by("studentName")
    return render(request, 'stu/result.html', {"form": form})


def editstudent(request, pk):
    form = Student.objects.get(id=pk)
    context = {"form": form}
    return render(request, 'stu/editprofile.html', context)


def deletestudent(request, student_id):
    student = Student.objects.get(pk=student_id)
    context = {"student": student}
    return render(request, 'stu/delete.html', context)
