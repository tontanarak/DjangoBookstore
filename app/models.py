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
    index = models.CharField(max_length=4)
    UserID = models.ForeignKey(User,on_delete=models.CASCADE)
    BookID = models.ForeignKey(Book,on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
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
    def __str__(self):
        return self.index

    
    


    

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    BookID = models.ForeignKey(Book,on_delete=models.CASCADE)
    UserID = models.ForeignKey(User,on_delete=models.CASCADE)
    CartQty = models.PositiveIntegerField()
    CartPrice = models.FloatField()
    
    

class confirm(models.Model):
    Name= models.CharField(max_length=300)
    payID= models.CharField(max_length=300)
    phoneNo = models.CharField(max_length=300)
    date =  models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    note = models.CharField(max_length=300)



