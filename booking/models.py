from django.db import models

from organisations.models import Organisation, OpeningHour

# Create your models here.
class Booking(models.Model):
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=8)
    booked_at = models.DateTimeField()
    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        blank=True
    )

    def __str__(self):
        return str((self.email, self.organisation.name))
