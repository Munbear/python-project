from django.db import models

# Create your models here.
class User(models.Model):
  username = models.CharField(max_length=64, verbose_name= 'Username')
  password = models.CharField(max_length=64, verbose_name= 'Password')
  register_dttm = models.DateTimeField(auto_now_add=True, verbose_name= 'RegisterTime')

  class Meta:
    db_table = 'TestUser'