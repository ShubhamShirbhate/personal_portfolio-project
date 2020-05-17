from django.db import models

class project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title



class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    memo = models.TextField()

    
    def __str__(self):
        return self.name
