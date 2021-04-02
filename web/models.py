from django.db import models

# Create your models here.

class Top5Institute(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(upload_to='media/institute/')
    disp = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Teachers = models.CharField(max_length=200)
    Subjects = models.CharField(max_length=200)
    Mobile = models.CharField(max_length=200)
    ListStudent = models.CharField(max_length=200)
    Time = models.CharField(max_length=200)
    Batchs = models.CharField(max_length=200)

    def __str__(self):
        return self.name
