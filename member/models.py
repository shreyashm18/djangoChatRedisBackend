from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avtar = models.ImageField(null=False, blank=False, max_length=20)

    def __str__(self):
        return self.user.first_name+' '+self.user.last_name