from django.db import models

# Create your models here.

class User(models.Model):
    FirstName = models.CharField(max_length=50, blank=False, null=False,)
    LastName = models.CharField(max_length=50, blank=False, null=False)
    Login = models.CharField(max_length=50, blank=False, unique=True, null=False)
    Password = models.CharField(max_length=50, blank=False, null=False)
    TotalScores = models.IntegerField(blank=True, default=0)



    def __str__(self):
        return self.FirstName + " " + self.LastName


class Question(models.Model):
    Question_text = models.CharField(max_length=255)
    Score = models.IntegerField()

    def __str__(self):
        return self.Question_text