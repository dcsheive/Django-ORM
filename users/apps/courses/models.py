from django.db import models

# Create your models here.
class Course(models.Model):
      name = models.CharField(max_length=255)
      text = models.TextField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)

# class Description(models.Model):
#       text = models.TextField()
#       created_at = models.DateTimeField(auto_now_add = True)
#       updated_at = models.DateTimeField(auto_now = True)
#       course = models.OneToOneField(Course, on_delete=models.CASCADE, primary_key= True)
