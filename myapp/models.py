from django.db import models

# Create your models here.
from django.db import models

class PriohubItem(models.Model):
    # product_distributor_name = models.CharField(max_length=255)
    # value_product_type_id = models.IntegerField()
    product_overbooking_allowed=models.BooleanField()
   

    def __str__(self):
        return self.product_distributor_namet
