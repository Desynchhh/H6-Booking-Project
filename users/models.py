from django.db import models

from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(
        "organisations.Organisation",
        on_delete=models.SET_DEFAULT,
        default=None,
        null=True
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"