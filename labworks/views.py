from django.shortcuts import render, get_object_or_404
from .models import LabWork


def labwork_list(request):
    labworks = LabWork.objects.all()
    return render(request, 'labworks/labwork_list.html', {'labworks': labworks})


def labwork_detail(request, slug):
    labwork = get_object_or_404(LabWork, slug=slug)
    return render(request, 'labworks/labwork_detail.html', {'labwork': labwork})
