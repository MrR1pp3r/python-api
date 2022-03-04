from django import views
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View, generic

from details.form import FormStudent
from details.models import Student
# Create your views here.


class DeleteForm(generic.DeleteView):
    template_name = "stu/delete.html"
    model = Student
    success_url = "delete"


class DemoForm(View):
    def get(self, request):
        return render(request, 'stu/demoget.html')

    def post(self, request):
        return render(request, 'stu/demopost.html')


def index(request):
    form = FormStudent(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("stud:result"))

    context = {"form": form}
    return render(request, 'stu/index.html', context)


def result(request):
    form = Student.objects.order_by("id")
    context = {
        "form": form,
    }
    return render(request, 'stu/result.html', context)


def editstudent(request, pk):
    form_id = Student.objects.get(pk=pk)
    form = FormStudent(request.POST or None, instance=form_id)
    if form.is_valid():
        if form.changed_data:
            form.save()
            return HttpResponseRedirect(reverse("stud:result"))
        return HttpResponse("DATA NOT CHANGED")

    context = {"form": form}
    return render(request, 'stu/edit.html', context)


def deletestudent(request, pk):
    form_id = Student.objects.get(pk=pk)
    postdata = FormStudent(request.POST or None, instance=form_id)
    if postdata.is_valid() == False:
        form_id.delete()
        return HttpResponseRedirect(reverse("stud:result"))

    return render(request, 'stu/delete.html')
# return HttpResponseRedirect(reverse("stud:result"))
