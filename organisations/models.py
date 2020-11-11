from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from django.utils.text import slugify

import re, datetime

def validate_is_phonenumber(num:int) -> bool:
    if isinstance(num, int):
        return len(str(num)) == 8
    return False


def validateTimeFormInput(time) -> bool:
    regex = re.compile(r'^[0-2]\d[:][0-5]\d([:][0-5]\d)?$')
    if not re.match(regex, str(time)):
        raise ValidationError('Tidsinput skal overholde følgende format: 00:00')


# Create your models here.
class Organisation(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField(validators=[validate_is_phonenumber])
    slug = models.SlugField(
        max_length=255,
        blank=True,
    )
    address = models.CharField(
        max_length=255,
    )
    website = models.CharField(
        max_length=255,
        default=None,
        null=True
    )
    image = models.ImageField(
        default=None,
        upload_to='organisations/',
        null=True
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class OpeningHours(models.Model):
    class DayChoices(models.TextChoices):
        MONDAY = (0, 'Mandag')
        TUESDAY = (1, 'Tirsdag')
        WEDNESDAY = (2, 'Onsdag')
        THURSDAY = (3, 'Torsdag')
        FRIDAY = (4, 'Fredag')
        SATURDAY = (5, 'Lørdag')
        SUNDAY = (6, 'Søndag')

    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    day = models.CharField(max_length=1, choices=DayChoices.choices, default=None)
    time_open = models.TimeField(default=None, validators=[validateTimeFormInput])
    working_time = models.CharField(max_length=255, validators=[validateTimeFormInput])
    
    @property
    def get_day(self):
        return self.get_day_display()

    @property
    def get_closing_hours(self):
        time_open_hours, time_open_minutes, *_ = str(self.time_open).split(':')
        time_open_delta = datetime.timedelta(hours=int(time_open_hours), minutes=int(time_open_minutes))
        return str(time_open_delta + datetime.timedelta(minutes=int(self.working_time)))[:5]

    def __str__(self):
        return f'{self.organisation.name} ({self.day}, {self.time_open}, {self.working_time})'
    