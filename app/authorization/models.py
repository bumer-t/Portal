from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Profile(models.Model):
    user_id = models.ForeignKey(User)
    name = models.CharField(max_length=20)
    pub_date = models.DateTimeField()
    sex = models.IntegerField()
    sity = models.CharField(max_length=40)
    email = models.EmailField(blank=True, verbose_name='e-mail')
    img = models.CharField(max_length=40)
    
    class Admin:
        pass
    
    def __unicode__(self):
        return self.name