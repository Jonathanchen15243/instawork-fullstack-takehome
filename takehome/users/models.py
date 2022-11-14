from django.db import models
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.PositiveBigIntegerField()
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return HttpResponseRedirect(reverse_lazy('users:index'))