from django.db import models

# Create your models here.


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    BookName = models.CharField(max_length=300)
    BookAuthor = models.CharField(max_length=200)
    BookDesc = models.TextField()
    BookPrice = models.IntegerField()
    BookQty = models.IntegerField()



    