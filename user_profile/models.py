from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE) # OneToOne relation
    address = models.TextField(null=True, blank=True)
    mobile =models.CharField(max_length=10, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self) :
        return str(self.user.id)