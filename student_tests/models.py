from django.db import models
from django.utils.text import slugify
from unidecode import unidecode


class Test(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(unidecode(self.title))
            unique_slug = original_slug
            num = 1
            while Test.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{original_slug}-{num}'
                num += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField(default='')
    image = models.FileField(
        upload_to='question_images/', blank=True, null=True)
    test = models.ForeignKey(
        Test, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class TestResult(models.Model):
    test = models.ForeignKey(
        Test, related_name='results', on_delete=models.CASCADE)
    # Добавлено поле для имени пользователя
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.test.title} - {self.score} баллов"
