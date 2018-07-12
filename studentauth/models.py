from django.db import models

# Create your models here.


class Student(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

    def __str__(self):
        """A string representation of the model."""
        return 'Welcome: ' + self.fullname
