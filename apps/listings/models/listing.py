from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models

from apps.base.timestamp import TimestampModel


class Listing(TimestampModel):

    class PropertyType(models.TextChoices):
        APARTMENT = "apartment", "Apartment"
        HOUSE = "house", "House"
        STUDIO = "studio", "Studio"
        OTHER = "other", "Other"
        ROOM = "room", "Room"

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="listings"
    )

    title = models.CharField(max_length=255)
    description = models.TextField()

    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=5)
    unit = models.CharField(max_length=100, blank=True)
    floor = models.SmallIntegerField(null=True, blank=True)

    has_balcony = models.BooleanField(default=False)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))]
    )

    rooms = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    property_type = models.CharField(
        max_length=20,
        choices=PropertyType.choices
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Listing"
        verbose_name_plural = "Listings"

        ordering = ["-created_at"]

        constraints = [
            models.CheckConstraint(
                condition=models.Q(price__gte=Decimal("0.01")),
                name="listing_price_gte_001"
            ),
            models.CheckConstraint(
                condition=models.Q(rooms__gte=1),
                name="listing_rooms_gte_1"
            ),
        ]

    def __str__(self):
        return self.title