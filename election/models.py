from django.db import models

class Election(models.Model):
    Election_ID = models.CharField(default = "", max_length=200)
    Name = models.CharField(default = "", max_length=200)
    Number_Of_Questions = models.IntegerField(default = 0)
    Description = models.TextField(default = "")
    Vote_Count = models.IntegerField(default = 0)
    Election_Method = models.CharField(default = "", max_length=200)
    Owner = models.CharField(default = "", max_length=200)
    #Alternatives? Spør Jesse

    def __str__(self):
        return self.Election_ID

class Question(models.Model):
    Election_ID = models.CharField(default = "", max_length=200)
    Question_ID = models.CharField(default = "", max_length=200)
    Wording = models.TextField(default = "")
    Vote_Count = models.IntegerField(default = 0)
    Election_Method = models.CharField(default = "", max_length=200)
    Number_Of_Alternatives = models.IntegerField(default = 1)
    Owner = models.CharField(default = "", max_length=200)

    def __str__(self):
        return self.Question_ID


class Alternative(models.Model):
    Question_ID = models.CharField(default = "", max_length=200)
    Wording = models.CharField(default = "", max_length=200)
    Value = models.IntegerField(default = 0)
    Owner = models.CharField(default = "", max_length=200)

class Vote(models.Model):
    Election_ID = models.CharField(default = "", max_length=200)
    Alternative = models.CharField(default = "", max_length=200)
    Value = models.IntegerField(default = 0)





