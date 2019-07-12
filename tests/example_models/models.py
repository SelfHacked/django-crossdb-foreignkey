from django.db import models
from django_crossdb_foreignkey import CrossDBForeignKey, CrossDBOneToOneField


class Department(models.Model):
    code = models.CharField(max_length=6)


class OtherEmployee(models.Model):
    name = models.TextField()
    department = CrossDBForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='employees',
    )


class OtherManager(models.Model):
    name = models.TextField()
    department = CrossDBOneToOneField(
        Department,
        on_delete=models.DO_NOTHING,
        related_name='manager',
    )


class OtherSection(models.Model):
    name = models.TextField()
    department = CrossDBOneToOneField(
        'example_models.Department',
        on_delete=models.CASCADE,
        related_name='+',
    )


class OtherHeadOffice(models.Model):
    department = CrossDBOneToOneField(
        Department,
        on_delete=models.SET_NULL,
        related_name='head_office',
        null=True,
    )
