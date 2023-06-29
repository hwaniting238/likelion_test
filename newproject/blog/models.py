from django.db import models

class club(models.Model):
    name = models.CharField(max_length=20)
    intro = models.TextField()
    head = models.FloatField()
    
    def __str__(self):
        return self.title
    


# Create your models here.
