from __future__ import annotations
import random
from datetime import date
from django.db import models


class Player(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )

    CATEGORY_CHOICES = (
        ("Boys", "Boys"),
        ("Girls", "Girls"),
        ("Men", "Men"),
        ("Women", "Women"),
    )

    name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    playing_position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='player_photos/', blank=True, null=True, default='default_player.png')
    institution_name = models.CharField(max_length=200, help_text="School / College / Village name")

    registration_number = models.CharField(max_length=4, unique=True, editable=False)

    tournament_consent = models.ForeignKey(
        'tournaments.Tournament', on_delete=models.SET_NULL, null=True, blank=True,
        help_text="Tournament you agree to play in"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.registration_number})"

    def save(self, *args, **kwargs):
        if not self.registration_number:
            self.registration_number = self._generate_unique_code()
        super().save(*args, **kwargs)

    @staticmethod
    def _generate_unique_code() -> str:
        # Try up to a reasonable number of attempts to avoid collisions
        for _ in range(10000):
            code = f"{random.randint(0, 9999):04d}"
            if not Player.objects.filter(registration_number=code).exists():
                return code
        # Fallback (extremely unlikely)
        raise RuntimeError("Unable to generate unique registration number")

    @property
    def age(self) -> int:
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years
