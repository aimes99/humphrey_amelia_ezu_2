from django.shortcuts import render

from courseinfo.models import (
    Instructor,
    Section,
)


def instructor_list_view(request):
    instructor_list = Instructor.objects.all()
    # instructor_list = Instructor.objects.none()
    return render(request, 'courseinfo/instructor_list.html', {'instructor_list': instructor_list})


def section_list_view(request):
    section_list = Section.objects.all()
    # section_list = Section.objects.none()
    return render(request, 'courseinfo/section_list.html', {'section_list': section_list})
