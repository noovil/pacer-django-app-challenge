from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.user.email
