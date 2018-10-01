from django.db import models
from ..apps.users import User
from ..apps.reviews import ListingReview

# Create your models here.

class AbstractItem(models.Model)
    name = models.CharField(max_length=200)

class Listing(models.Model)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    base_item = models.ForeignKey(AbstractItem, blank=True)
    reviews = models.ManyToMany(ListingReview)

