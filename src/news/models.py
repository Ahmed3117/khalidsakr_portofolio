from django.db import models
from django.utils import timezone
class Notification(models.Model):
    PRIORITY_CHOICES = [
        ('urgent', 'طارئ'),
        ('normal', 'عادى'),
    ]

    title = models.CharField(max_length=255, verbose_name='العنوان')
    description = models.TextField(verbose_name='الوصف',null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الاضافة')
    date_start = models.DateTimeField(verbose_name='تاريخ البدء',null=True,blank=True)
    date_end = models.DateTimeField(verbose_name='تاريخ الانتهاء',null=True,blank=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='normal', verbose_name='الأولوية')
    status = models.BooleanField(default=True, verbose_name='الحالة')
    
    def is_current(self):
        now = timezone.now()
        check_date = False
        if self.date_start and self.date_end:
            if self.date_start <= now <= self.date_end:
                check_date = True
        else:
            if self.status:
                check_date = True
        return check_date
    class Meta:
        verbose_name = 'الإشعار'
        verbose_name_plural = 'الإشعارات'

    def __str__(self):
        return self.title
