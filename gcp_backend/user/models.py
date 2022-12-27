from django.db import models
from gcp_backend.utility import create_id,hash_password
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
        ADMIN =  "0", "admin"
        STUDENT =  "2", "student"
        CLUB_ADMIN =  "1" , "club_admin"
    

    id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=10, unique=True, blank=True, null=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, unique=True)
    # org_mail = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField( max_length=13,blank=True, null=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_locked = models.BooleanField(default=False)
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.STUDENT)
    is_verified = models.BooleanField(default=False)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
    # auto generate userid
    def save(self, *args, **kwargs):
        if not self.userid:
            self.userid = create_id('USR')
            if self.role == "0":
                self.password = hash_password(self.password)
        super(User, self).save(*args, **kwargs)

   