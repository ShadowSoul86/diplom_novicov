from django import template

register = template.Library()

@register.filter
def replace_images(content, images):
    for i, image in enumerate(images, start=1):
        if image:
            marker = f'[image{i}]'
            img_tag = f'<img src="{image.url}" alt="Image {i}" class="img-fluid custom-img mx-auto d-block">'  # Добавляем классы для центрирования
            content = content.replace(marker, img_tag)
    return content
