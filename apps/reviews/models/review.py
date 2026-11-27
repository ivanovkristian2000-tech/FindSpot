from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models

from apps.base.timestamp import TimestampModel


class Review(TimestampModel):

    reservation = models.OneToOneField(
        "reservations.Reservation",
        on_delete=models.CASCADE,
        related_name="review"
    )

    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    comment = models.TextField(max_length=2000)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

        ordering = ["-created_at"]

        constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    rating__gte=1,
                    rating__lte=5
                ),
                name="review_valid_rating"
            ),
        ]

    def __str__(self):
        return f"Review #{self.pk} - {self.rating}/5"
