from django.db import models

class User(models.Model):       # User database
    FirstName = models.CharField(max_length=50, blank=False, null=False,)
    LastName = models.CharField(max_length=50, blank=False, null=False)
    Login = models.CharField(max_length=50, blank=False, unique=True, null=False)
    Password = models.CharField(max_length=50, blank=False, null=False)
    TotalScores = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.FirstName + " " + self.LastName


class Question(models.Model):       # Questions database
    Question_text = models.CharField(max_length=255)
    Score = models.IntegerField()

    def __str__(self):
        return self.Question_text