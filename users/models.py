from django.db import models

from django.contrib.auth.models import User


class RoleManager(models.Manager):
    def get_all_roles(self):
        return self.all()

class Role(models.Model):
    objects = RoleManager()

    name = models.CharField(max_length=255, unique=True)
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

    @property
    def full_name(self):
        "Returns the person's full name."
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return f"{self.user.username}'s Profile"
