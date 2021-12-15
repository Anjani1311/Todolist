from django.db import models

# Create your models here.
class Task(models.Model):
    task_title=models.CharField(max_length=30)
    task_description=models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title

class Book(models.Model):
    book_name=models.CharField(max_length=30)
    book_auther=models.CharField(max_length=30)
    book_description=models.TextField(max_length=100,default='No desc')
    book_picture=models.ImageField()
    book_publisher=models.CharField(max_length=30)
    book_email=models.EmailField(blank=True)  #mandatory field
    book_price=models.IntegerField(default=0)

    def __str__(self):
        return self.book_name



