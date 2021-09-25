from django.db import models

# Create your models here.
class Task(models.Model):
    # PRIORITY = (('High','High'),
    #             ('Medium','Medium'),
    #             ('Low','Low'),)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False,blank=False,null=True)
    # priority = models.CharField(default="Low",max_length=20, null = False, choices=PRIORITY)

def __str__(self):
    return self.title