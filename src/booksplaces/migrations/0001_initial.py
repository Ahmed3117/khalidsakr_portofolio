# Generated by Django 5.0.6 on 2024-07-04 04:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('centersplaces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الاسم')),
                ('location', models.CharField(max_length=255, verbose_name='الموقع')),
                ('status', models.BooleanField(default=True, verbose_name='الحالة')),
                ('government', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centersplaces.government', verbose_name='المحافظة')),
            ],
            options={
                'verbose_name': 'المكتبة',
                'verbose_name_plural': 'المكتبات',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الاسم')),
                ('description', models.TextField(blank=True, null=True, verbose_name='الوصف')),
                ('status', models.BooleanField(default=True, verbose_name='الحالة')),
                ('class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centersplaces.class', verbose_name='الفصل')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booksplaces.library', verbose_name='المكتبة')),
            ],
            options={
                'verbose_name': 'الكتاب',
                'verbose_name_plural': 'الكتب',
            },
        ),
    ]
