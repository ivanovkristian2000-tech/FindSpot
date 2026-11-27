from django.conf import settings
from django.db import models

from apps.base.timestamp import TimestampModel


class Reservation(TimestampModel):

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        REJECTED = "rejected", "Rejected"
        CANCELLED = "cancelled", "Cancelled"
        COMPLETED = "completed", "Completed"

    renter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="reservations"
    )

    listing = models.ForeignKey(
        "listings.Listing",
        on_delete=models.CASCADE,
        related_name="reservations"
    )

    start_date = models.DateField()
    end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

        ordering = ["-created_at"]

        constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    end_date__gt=models.F("start_date")
                ),
                name="reservation_valid_dates"
            ),
        ]

    def __str__(self):
        return f"{self.renter} - {self.listing}"