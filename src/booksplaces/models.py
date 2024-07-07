from django.db import models
from centersplaces.models import Government, Class

class Library(models.Model):
    name = models.CharField(max_length=255, verbose_name='الاسم')
    government = models.ForeignKey(Government, on_delete=models.CASCADE, verbose_name='المحافظة')
    location = models.CharField(max_length=255, verbose_name='الموقع')
    status = models.BooleanField(default=True, verbose_name='الحالة')

    class Meta:
        verbose_name = 'المكتبة'
        verbose_name_plural = 'المكتبات'

    def __str__(self):
        return self.name

class LibraryContact(models.Model):
    library = models.ForeignKey(Library, on_delete=models.CASCADE, verbose_name='المكتبة')
    phone = models.CharField(max_length=255, verbose_name=' التليفون')
    mail = models.EmailField(max_length=255, verbose_name='الايميل')

    class Meta:
        verbose_name = 'وسيلة تواصل'
        verbose_name_plural = 'وسائل التواصل'

    def __str__(self):
        return self.phone

class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name='الاسم')
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='الفصل')
    library = models.ForeignKey(Library, on_delete=models.CASCADE, verbose_name='المكتبة')
    description = models.TextField(blank=True, null=True, verbose_name='الوصف')
    status = models.BooleanField(default=True, verbose_name='الحالة')
    

    class Meta:
        verbose_name = 'الكتاب'
        verbose_name_plural = 'الكتب'

    def __str__(self):
        return self.name
