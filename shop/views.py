from django.shortcuts import get_object_or_404, render

from .models import Course

TEMPLATE_PREFIX = 'shop/'


def index(request):
    courses = Course.objects.all()
    return render(
        request,
        template_name=f'{TEMPLATE_PREFIX}courses.html',
        context={'courses': courses}
        )


def single_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(
        request,
        template_name=f'{TEMPLATE_PREFIX}single_course.html',
        context={'course': course}
        )
