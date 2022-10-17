from tkinter import CASCADE
from unicodedata import name
from django.db import models
from Projects.models import Project

class MatrialInvoice(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE, related_name="matrial" )
    invoiceNumber =models.CharField(max_length = 200)
    date = models.DateField()
    amount = models.DecimalField(max_digits=50, decimal_places=2)

