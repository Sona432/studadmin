from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(max_length=8)
    physics = models.IntegerField(default=0)
    chemistry = models.IntegerField(default=0)
    maths = models.IntegerField(default=0)
    computer_science = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    perecent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    