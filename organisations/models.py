from django.db import models

from django.utils.text import slugify


def validate_is_phonenumber(num:int) -> bool:
    print(num)
    return False
    if isinstance(num, int):
        return len(str(num)) == 8
    return False


# Create your models here.
class Organisation(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, )
    phone = models.IntegerField(validators=[validate_is_phonenumber])
    slug = models.SlugField(
        max_length=255,
        blank=True,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
