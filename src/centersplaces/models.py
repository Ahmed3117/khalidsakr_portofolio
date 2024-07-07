import datetime
from django.db import models

class Government(models.Model):
    name = models.CharField(max_length=255, verbose_name='الاسم')

    class Meta:
        verbose_name = 'محافظة'
        verbose_name_plural = 'المحافظات'

    def __str__(self):
        return self.name

class Center(models.Model):
    name = models.CharField(max_length=255, verbose_name='الاسم',default='بدون اسم')
    government = models.ForeignKey(Government, on_delete=models.CASCADE, verbose_name='المحافظة')
    location = models.CharField(max_length=255, verbose_name='الموقع')
    status = models.BooleanField(default=True, verbose_name='الحالة')

    class Meta:
        verbose_name = 'سنتر'
        verbose_name_plural = 'السناتر'

    def __str__(self):
        return self.location

class CenterContact(models.Model):
    center = models.ForeignKey(Center, on_delete=models.CASCADE, verbose_name='السنتر')
    phone = models.CharField(max_length=255, verbose_name=' التليفون')
    mail = models.EmailField(max_length=255, verbose_name='الايميل')

    class Meta:
        verbose_name = 'وسيلة تواصل'
        verbose_name_plural = 'وسائل التواصل'

    def __str__(self):
        return self.phone


class Class(models.Model):
    name = models.CharField(max_length=255, verbose_name='الاسم')
    status = models.BooleanField(default=True, verbose_name='الحالة')

    class Meta:
        verbose_name = 'صف'
        verbose_name_plural = 'الصفوف'

    def __str__(self):
        return self.name

class Dates(models.Model):
    """Model representing a date for a class at a center."""

    DAYS = (
        ('1', 'الأحد'),
        ('2', 'الاثنين'),
        ('3', 'الثلاثاء'),
        ('4', 'الاربعاء'),
        ('5', 'الخميس'),
        ('6', 'الجمعة'),
        ('7', 'السبت'),
    )

    center = models.ForeignKey(Center, on_delete=models.CASCADE, verbose_name='السنتر')
    status = models.BooleanField(default=True, verbose_name='الحالة')
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='الصف')
    date_day = models.CharField(max_length=255, choices=DAYS, default='1', verbose_name='اليوم')
    date_time = models.TimeField(verbose_name='الساعة', default=datetime.time(hour=6, minute=0))


    class Meta:
        verbose_name = 'موعد'
        verbose_name_plural = 'المواعيد'

    def __str__(self):
        return f"{self.center.name} - {self.class_obj.name} - {self.get_date_day_display()} - {self.date_time}"


