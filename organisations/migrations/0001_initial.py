# Generated by Django 3.1.3 on 2020-11-06 11:39

from django.db import migrations, models
import organisations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField(validators=[organisations.models.validate_is_phonenumber])),
                ('slug', models.SlugField(blank=True, max_length=255)),
                ('address', models.CharField(default=None, max_length=255, null=True)),
                ('website', models.CharField(default=None, max_length=255, null=True)),
                ('image', models.ImageField(default=None, null=True, upload_to='organisations/')),
            ],
        ),
    ]
