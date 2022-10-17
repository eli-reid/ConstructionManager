
from pyexpat import model
from django.db import models

class Address(models.Model):
    street = models.CharField(max_length = 200)
    unit = models.CharField(max_length = 200, blank = True)
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    zip = models.CharField(max_length = 200)


class Project(models.Model):
    BID = 'B'
    ACCEPTED = 'A'
    STARTED = 'S'
    CLOSED = 'C'
    STATUS_CHOICES = [(BID, 'Bid'), (ACCEPTED, 'Accepted'), (STARTED, 'Started'), (CLOSED, 'Closed'),]
    created = models.DateTimeField(auto_now_add = True)
    name = models.CharField(max_length = 200)
    po = models.BigIntegerField()
    permitNumber = models.CharField(max_length = 200, blank = True)
    bidNumber = models.DecimalField(max_digits=50, decimal_places=2)
    address = models.ForeignKey(Address, on_delete = models.CASCADE)
    status = models.CharField(max_length = 3 , choices = STATUS_CHOICES, default = BID)
    contractCompleteDate= models.DateField()
    projectedStartDate = models.DateField()



