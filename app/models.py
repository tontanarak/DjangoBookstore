from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#table User is Create By django Auth.

class Book(models.Model):
    id = models.AutoField(primary_key=True ,serialize=False)
    BookName = models.CharField(max_length=300)
    BookAuthor = models.CharField(max_length=200)
    BookDesc = models.TextField()
    BookPrice = models.FloatField()
    BookQty = models.PositiveIntegerField()
    BookPic = models.CharField(max_length=200)
    


class Payment(models.Model):
    id = models.AutoField(primary_key=True,unique=False)
    UserID = models.ForeignKey(User,on_delete=models.CASCADE)
    Total = models.PositiveIntegerField()
    Address = models.TextField()

    WAITING = 'Waiting'
    CANCEL = 'Cancel'
    DONE = 'Done'
    PAYMENT_STATUS = [
        (WAITING,'Waiting'),
        (CANCEL,'Cancel'),
        (DONE,'Done'),
    ]
    Status = models.CharField(
        max_length=10,
        choices=PAYMENT_STATUS,
        default=WAITING,
    )
    


    

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    BookID = models.ForeignKey(Book,on_delete=models.CASCADE)
    UserID = models.ForeignKey(User,on_delete=models.CASCADE)
    CartQty = models.PositiveIntegerField()
    CartPrice = models.FloatField()
    
    





