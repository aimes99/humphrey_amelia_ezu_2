from django.shortcuts import render
from django.views import View

from .models import (
    Instructor,
    Section,
    Course,
    Semester,
    Student,
    Registration,
)


class InstructorList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/instructor_list.html',
            {'instructor_list': Instructor.objects.all()}
        )


class SectionList(View):

    def get(self, request):
        return render(
            request,
            'courseinfo/section_list.html',
            {'section_list': Section.objects.all()}
        )


def course_list_view(request):
    course_list = Course.objects.all()
    # course_list = Course.objects.none()
    return render(request, 'courseinfo/course_list.html', {'course_list': course_list})


def semester_list_view(request):
    semester_list = Semester.objects.all()
    # semester_list = Semester.objects.none()
    return render(request, 'courseinfo/semester_list.html', {'semester_list': semester_list})


def student_list_view(request):
    student_list = Student.objects.all()
    # student_list = Student.objects.none()
    return render(request, 'courseinfo/student_list.html', {'student_list': student_list})


def registration_list_view(request):
    registration_list = Registration.objects.all()
    # registration_list = Registration.objects.none()
    return render(request, 'courseinfo/registration_list.html', {'registration_list': registration_list})
