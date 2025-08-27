from django.db import models

# Create your models here.
class Billing(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled'),
    ]

    owner_id   = models.IntegerField()
    type = models.CharField(max_length=200)
    type_name = models.CharField(max_length=200)
    pet_id = models.IntegerField()
    payment = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')

    class Meta:
        unique_together = ('owner_id', 'pet_id', 'type')

    def __str__(self):
        return str(self.owner_id)

class CheckList(models.Model):
    invalid_name = models.CharField(max_length=200)

    class Meta:
        db_table = 'check_list'
