from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key = True)
    ename = models.CharField(max_length = 100)
    sal = models.IntegerField()
    job = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.ename