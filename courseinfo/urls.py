from django.urls import path

from courseinfo.views import (
    semester_list_view,
    course_list_view,
    student_list_view,
    registration_list_view,
    InstructorList,
    SectionList,
)

urlpatterns = [

    path('instructor/',
         InstructorList.as_view(),
         name='courseinfo_instructor_list_urlpattern'),

    path('section/',
         SectionList.as_view(),
         name='courseinfo_section_list_urlpattern'),


    path('course/', course_list_view),
    path('semester/', semester_list_view),
    path('student/', student_list_view),
    path('registration/', registration_list_view),
]
