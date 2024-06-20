from django.shortcuts import render, get_object_or_404
from .models import Lecture


def lecture_list(request):
    lectures = Lecture.objects.all()
    return render(request, 'lectures/lecture_list.html', {'lectures': lectures})


def lecture_detail(request, slug):
    lecture = get_object_or_404(Lecture, slug=slug)
    return render(request, 'lectures/lecture_detail.html', {'lecture': lecture})
