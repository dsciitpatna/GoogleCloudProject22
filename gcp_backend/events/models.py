from django.db import models
from user.models import Organization, User
# Create your models here.

class Type(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.type

class Tag (models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.tag


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    # is_verified = models.BooleanField(default=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    type = models.ForeignKey('Type', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    social_links = models.TextField(blank=True, null=True)
    rsvp_link = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name