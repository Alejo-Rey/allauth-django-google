from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    phone_number = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(
        upload_to='users/pictures', blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    id_employee = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=30, blank=True)
    civil_status = models.CharField(max_length=30, blank=True)
    nss = models.CharField(max_length=30, blank=True)
    sin = models.CharField(max_length=30, blank=True)
    nin = models.CharField(max_length=30, blank=True)
    taxpayer_number = models.CharField(max_length=30, blank=True)
    shirt_size = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    cell_phone_number = models.CharField(max_length=20, blank=True)
    work_phone_number = models.CharField(max_length=20, blank=True)
    work_email = models.EmailField(max_length=254, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    birthdate = models.CharField(max_length=30, blank=True)


class Education(models.Model):
    """
    All the type of education of the user
    """

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, blank=True)
    start_year = models.DateField(blank=True)
    end_year = models.DateField(blank=True)
    description = models.TextField(blank=True)

    def __str__ (self):
        """
        return name of school
        """
        return self.school