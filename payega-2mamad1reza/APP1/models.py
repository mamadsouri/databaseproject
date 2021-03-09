from django.db import models
from django.contrib.auth.models import User


class AddressUny(models.Model):

    address1 = models.CharField("Address line 1", max_length=1024)

    zip_code = models.CharField("ZIP / Postal code", max_length=12)

    city = models.CharField("City", max_length=1024,)

    st = models.CharField("street", max_length=20)


class University(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    addres = models.ForeignKey(AddressUny, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Name


class Professor(models.Model):
    Email_p = models.EmailField()
    Degree_of_education_p = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    uni = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    name_p = models.CharField(max_length=50, null=True, blank=True)
    family_p = models.CharField(max_length=50, null=True, blank=True)
    age_p = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name_p


class Student(models.Model):
    Email_s = models.EmailField()
    degree_of_education_p = models.FileField(upload_to='media/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True, blank=True)
    number_of_student = models.IntegerField(null=True, blank=True, unique=True)
    uni = models.ForeignKey(University, on_delete=models.CASCADE, null=True, blank=True)
    name_s = models.CharField(max_length=50, null=True, blank=True)
    family_s = models.CharField(max_length=50, null=True, blank=True)
    age_s = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name_s


class Maghale(models.Model):
    Code_Maghale = models.IntegerField()
    title_Maghale = models.CharField(max_length=200)
    Grouping_Maghale = models.CharField(max_length=200)
    Professor_Maghale = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to='media/', null=True, blank=True)
    like = models.ManyToManyField(User, related_name='Blogliks', blank=True)
    ShortExplanation = models.TextField(null=True, blank=True)
    choise = [
        ('like', 'like'),
        ('dislike', 'dislike'),
    ]
    vaziat = models.CharField(max_length=20, choices=choise, null=True)

    def __str__(self):
        return self.title_Maghale
    
    def getsnippet(self):
        return self.ShortExplanation[0:100] + '...'    

class AboutUs(models.Model):
    title_A = models.CharField(max_length=100, null=True, blank=True)
    conrext_A = models.CharField(max_length=1000, null=True, blank=True)
