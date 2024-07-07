from django.db import models
from django.core.validators import RegexValidator
from admin_interface.models import Theme

def default_logo():
    try:
        # Get the first Theme object
        theme = Theme.objects.first()
        if theme and theme.logo:
            return theme.logo.url  # Assuming 'logo' is an ImageField
    except Theme.DoesNotExist:
        pass
    return 'static\imgs\logo\default_logo.png'  # Fallback if no theme or logo exists


class Account(models.Model):
    logo = models.ImageField(upload_to='accounts/logos/', blank=True, null=True, editable=False, default=default_logo, verbose_name='الشعار')
    name = models.CharField(max_length=255, verbose_name='الاسم')
    description = models.TextField(blank=True, null=True, verbose_name='الوصف')
    caption = models.CharField(max_length=255, blank=True, null=True, verbose_name='التعليق')
    image = models.ImageField(upload_to='accounts/', blank=True, null=True, verbose_name='الصورة')
    mail = models.EmailField(verbose_name='البريد الإلكتروني')
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name='العنوان')

    class Meta:
        verbose_name = 'البيانات الشخصية'
        verbose_name_plural = 'البيانات الشخصية'

    def __str__(self):
        return self.name

class Phone(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='الحساب')
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$')], verbose_name='رقم الهاتف')

    def __str__(self):
        return self.phone_number

class SocialAccount(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='الحساب')
    site = models.CharField(max_length=255, verbose_name='الموقع')
    url = models.URLField(verbose_name='الرابط')
    icon = models.FileField(upload_to='social_icons/', blank=True, null=True, verbose_name='الأيقونة')
    is_active = models.BooleanField(default=True, verbose_name='نشط')

    def __str__(self):
        return f"{self.site} - {self.url}"
