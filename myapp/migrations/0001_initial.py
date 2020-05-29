# Generated by Django 2.2.12 on 2020-05-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COMPANY_NAME', models.CharField(blank=True, max_length=255)),
                ('FRONT_INSIDE_PICTURE', models.FileField(upload_to='documents/')),
                ('BUSINESS_CARD_IMAGE', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
