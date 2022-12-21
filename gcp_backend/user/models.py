from django.db import models

class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
 
class User(models.Model):
    class Role(models.TextChoices):
        ADMIN = "admin", "0"
        STUDENT = "student", "2"
        CLUB_ADMIN = "club_admin", "1"
    

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    # org_mail = models.CharField(max_length=100, unique=True)
    ph_num = models.CharField( max_length=13,blank=True, null=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.STUDENT)
    # is_verified = models.BooleanField(default=False)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

