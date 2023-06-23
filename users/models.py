from django.contrib.auth.models import AbstractUser, Group as BaseGroup


class User(AbstractUser):
    pass


class Group(BaseGroup):
    class Meta:
        proxy = True
        verbose_name = BaseGroup._meta.verbose_name
        verbose_name_plural = BaseGroup._meta.verbose_name_plural
