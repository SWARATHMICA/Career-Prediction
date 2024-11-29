from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=[
        ('Technical', 'Technical'),
        ('Creative', 'Creative'),
        ('Management', 'Management'),
    ])

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    value = models.IntegerField()  # E.g., -1, 0, 1 for scoring

    def __str__(self):
        return self.text

class Recommendation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recommended_career = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
