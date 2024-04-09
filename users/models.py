from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager

from store.models import Book


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_("Email address"), unique=True)
    is_staff = models.BooleanField(default=False, verbose_name=_("Is staff?"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is active?"))
    date_joined = models.DateTimeField(default=timezone.now, verbose_name=_("Date joined"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# Create a many-to-many relationship cart model to store items
class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name=_("User"))
    books = models.ManyToManyField(Book, related_name="cart", verbose_name=_("Books"))
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name=_("Total"))

    def __str__(self):
        return f"Cart for {self.user.email}"
