from django.db import models
from uuid import uuid4
# Create your models here.


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_lenth=20)
    email = models.EmailField(max_length=254)
    sprint_challenge = models.ForeignKey(
        Sprint_Challenge, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    student_review = models.TextField()
    pm = models.ForeignKey(PM, on_delete=models.CASCADE)


class Rating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    student_rating = models.IntegerField(min_value=1, max_value=3)
    pm_rating = models.IntegerField(min_value=1, max_value=2)


class PM(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_lenth=20)
    email = models.EmailField(max_length=254)


class Sprints(models.Model):
    name = models.CharField(max_length=30, editable=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
