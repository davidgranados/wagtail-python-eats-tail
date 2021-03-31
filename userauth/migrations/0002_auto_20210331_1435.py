# Generated by Django 3.0.13 on 2021-03-31 14:35

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['last_name']},
        ),
        migrations.AddField(
            model_name='customuser',
            name='additional_information',
            field=models.CharField(blank=True, max_length=4096, null=True, verbose_name='Additional information'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='address1',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 1'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='address2',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 2'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of birth'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='display_name',
            field=models.CharField(default='anonymous', help_text='Will be shown e.g. when commenting', max_length=30, verbose_name='Display name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='mobile_phone',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Enter a valid international mobile phone number starting with +(country code)', regex='^\\+(?:[0-9]●?){6,14}[0-9]$')], verbose_name='Mobile phone'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(default='photos/default-user-avatar.png', upload_to='photos/', verbose_name='Photo'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='zip_code',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Postal Code'),
        ),
    ]
