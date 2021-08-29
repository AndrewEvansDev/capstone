from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=35)
    desc = models.CharField(null=False, blank=True, max_length=200)
    type = models.CharField(null=False, blank=True, max_length=25)
    date = models.DateField(auto_now=False, auto_now_add=True)
    in_stock = models.BooleanField(default=False)
    in_stock_amount = models.IntegerField(default=0)

#     pairings = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+')
#     author = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
#     locations_used = ManyToManyField(WorkSite, blank=True, related_name="locations")

    def __str__(self):
        return self.name

    def __repr__(self):
        return "%s, %s" % (self.name, self.type)

class Rental(models.Model):
    pass

class Paint(Product):
    gallon_price = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=2)
    five_gallon_price = models.DecimalField(blank=True, max_digits=6, decimal_places=2, null=True)
    custom = models.BooleanField(null=False, blank=True)
