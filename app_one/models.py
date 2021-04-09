from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

            
        if len(postData['f_name']) < 2:
            errors['f_name'] = "First name must be at least 2 characters"


        if len(postData['l_name']) < 2:
            errors['l_name'] = "Last name must be at least  characters"


        if len(postData['email']) < 1:
            errors['email'] = "Email cannot be empty you suck"
        if not EMAIL_REGEX.match(postData['email']):   
            errors['email'] = "Invalid email address you suck"
        

        if len(postData['pw']) < 8:
            errors['pw_len'] = "Password should be at least 8 characters"
        if postData['pw'] != postData['confirm_pw']:
            errors['con_pw'] = "Password confirmation must match the password"


        return errors

    def login_validator(self, postData):
        errors = {}
        email = postData['email']
        pw = postData['pw']
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


        date = User.objects.filter(email = email)

        if len(email) < 1:
            errors['email'] = "Email cannot be empty you suck"
        elif not EMAIL_REGEX.match(postData['email']):   
            errors['email'] = "Invalid email address you suck"

        if len(pw) < 8:
            errors['pw'] = "Password shoudl be at least 8 characters"



        return errors



class User(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    pw = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()