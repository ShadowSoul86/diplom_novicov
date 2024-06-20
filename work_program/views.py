from django.shortcuts import render, redirect
from django.http import Http404
import os
from django.conf import settings
from pdf2image import convert_from_path


def work_program_view(request):
    return render(request, 'work_program/work_program.html')


def get_image_paths(pdf_name):
    """Возвращает список путей к изображениям для данного PDF файла."""
    image_paths = []
    for filename in os.listdir(settings.MEDIA_ROOT):
        if filename.startswith(pdf_name) and filename.endswith('.png'):
            image_paths.append(os.path.join(settings.MEDIA_ROOT, filename))
    return sorted(image_paths)


def convert_pdf_to_images(pdf_path, pdf_name):
    """Конвертирует PDF в изображения и сохраняет их."""
    images = convert_from_path(pdf_path)
    image_paths = []
    for i, image in enumerate(images):
        image_path = os.path.join(settings.MEDIA_ROOT, f'{pdf_name}_{i}.png')
        image.save(image_path, 'PNG')
        image_paths.append(image_path)
    return image_paths


def pdf_view(request, pdf_name):
    pdf_path = os.path.join(settings.MEDIA_ROOT, f'{pdf_name}.pdf')
    if not os.path.exists(pdf_path):
        raise Http404("PDF not found")

    # Установим заголовок страницы в зависимости от имени PDF файла
    page_titles = {
        'fos': 'ФОС',
        'work_program': 'Рабочая программа настройки и обеспечение функционирования программных средств и компьютерных систем и комплексов'
    }
    page_title = page_titles.get(pdf_name, 'Просмотр PDF')

    # Проверка, существуют ли уже изображения для данного PDF
    image_paths = get_image_paths(pdf_name)
    if not image_paths:
        try:
            image_paths = convert_pdf_to_images(pdf_path, pdf_name)
        except Exception as e:
            raise Http404(f"Error converting PDF: {e}")

    image_urls = [os.path.join(settings.MEDIA_URL, os.path.basename(
        image_path)) for image_path in image_paths]
    pdf_url = f'{settings.MEDIA_URL}{pdf_name}.pdf'
    return render(request, 'work_program/pdf_view.html', {
        'image_urls': image_urls,
        'pdf_name': pdf_name,
        'pdf_url': pdf_url,
        'page_title': page_title
    })
