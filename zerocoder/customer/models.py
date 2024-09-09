from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser

class Account(AbstractBaseUser):
    """
    Custom user class inheriting AbstractBaseUser class
    """

    f_name = models.CharField(verbose_name="Имя", max_length=255, default="")
    l_name = models.CharField(verbose_name="Фамилия", max_length=255, default="")
    shipping_address = models.CharField(verbose_name="Адрес доставки", max_length=255, default="")
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    phone_regex = RegexValidator(regex=r"^\+?1?\d{9,15}$")
    phone_number = models.CharField(
        verbose_name="Телефон",
        validators=[phone_regex],
        max_length=15,
        blank=True,
        default="",
        unique=True,
    )
    username = models.CharField(verbose_name="Логин", max_length=30, unique=True)
    slug = AutoSlugField(populate_from="username", default="", blank=True, null=True)
    date_joined = models.DateTimeField(
        verbose_name="Дата регистрации", auto_now_add=True
    )
    last_login = models.DateTimeField(
        verbose_name="Последний раз был онлайн", auto_now=True
    )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = MyAccountManager()

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
