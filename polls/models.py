from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 10)
    name = models.CharField(max_length = 25)

    email = models.EmailField(max_length = 35)
    dob = models.DateField()
    password = models.CharField(max_length = 10)

    def __str__(self):
        return self.name
    def user_name(self):
        return self.username
    def email_str(self):
        return self.email
    def date_of_birth(self):
        return self.dob
    def pass_word(self):
        return self.password
    
class Candidates(models.Model):
    cand_name = models.CharField(max_length=200)
    cand_text = models.TextField(default = "No Description")
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.cand_name