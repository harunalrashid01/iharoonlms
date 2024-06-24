from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="course/")
    def __str__(self):
        return self.name
    def image_tag(self):
        return format_html("<img src='/media/{}' style='width:40px;height:40px;' ".format(self.image)) 



class Subject(models.Model):
    name=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE) 
    def __str__(self):
        return self.name
  



class Chapter(models.Model):
    name=models.CharField(max_length=100)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)  
    content=HTMLField() 
 


    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
class Quiz(models.Model):
    name=models.CharField( max_length=50)
    chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE)

class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    question=HTMLField() 
    answer=models.IntegerField()

