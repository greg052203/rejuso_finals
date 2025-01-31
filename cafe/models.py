from django.db import models

class Order(models.Model):
    ITEM_CHOICES = [
        ('Smoked Bangus', 120.00),
        ('Breaded Liempo', 150.00),
        ('Longganisa', 100.00),
        ('Bites', 99.00),
        ('Tocino', 120.00),
        ('Porkchop', 125.00),
    ]

    item = models.CharField(max_length=100, choices=[(item[0], item[0]) for item in ITEM_CHOICES])
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Automatically set the price based on the selected item
        prices = dict(self.ITEM_CHOICES)
        self.price = prices.get(self.item, 0.00)

        # Calculate the total
        self.total = self.quantity * self.price

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.item} - {self.quantity}"


class Payment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment on {self.timestamp} - Amount: {self.total_amount}"
