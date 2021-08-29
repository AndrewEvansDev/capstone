
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    balance = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    banned = models.BooleanField(null=False, blank=True)
#    paints_logged = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    # address_home = AddressField(null=True)
    # address_work = AddressField(null=True)
    phone = models.IntegerField(null=True)
#     occupation = models.CharField(null=True, max_length=100)
#     regular_customer = models.BooleanField(null=False, blank=True)
#     referral_source = models.CharField(null=True, max_length=20, required=False)
#     paints_purchased = models.ForeignKey(Product, on_delete=models.CASCADE)

# fields = ('username','phone','email','address_home','address_work','occupation','referral_source','balance','banned','regular_customer',)


