from django.db import models
from special_offer.models import SpecialOffer
from user.models import User

class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending Payment'),
        ('paid', 'Paid'),
        ('confirmed', 'Enrollment Confirmed'),
    )

    special_offers = models.ForeignKey(SpecialOffer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_ordered = models.DateField()
    status = models.CharField(max_length=11, choices=STATUS_CHOICES)

    @property
    def product_name(self):
        return self.special_offers.product.name

    @property
    def product_image(self):
        return self.special_offers.image.url


