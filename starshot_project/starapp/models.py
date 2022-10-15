from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Upload(models.Model):

    file=models.FileField(upload_to='doc')
    # name=models.CharField(max_length=30)

    user_id=models.OneToOneField(User,on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.name
