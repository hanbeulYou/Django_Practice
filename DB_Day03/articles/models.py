from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    issue_a = models.CharField(max_length=20)
    issue_b = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    BLUE = 'BL'
    RED = 'RE'
    COLOR_CHOICES = [
        (BLUE, 'blue'),
        (RED, 'red'),
    ]
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    pick = models.CharField(
        max_length=2,
        choices=COLOR_CHOICES,
        default=BLUE,
    )
    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content