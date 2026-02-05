from django.db import models

# Create your models here.

class MPost(models.Model):
   img = models.ImageField(upload_to='images/')
   title = models.CharField (max_length=50)
   text = models.TextField()

   def __str__(self):
       return self.title
   


class MNews(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    img = models.ImageField(upload_to='images/')    
    def __str__(self):
       return self.title

class ACards(models.Model):
    img = models.ImageField(upload_to='images/')
    
    text = models.TextField()
    def __str__(self):
       return self.text

class Events (models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    text = models.TextField()  
    def __str__(self):
       return self.title      

class Races (models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    text = models.TextField()  
    def __str__(self):
       return self.title      

class Partner(models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    
    def __str__(self):
       return self.title