# Generated by Django 3.2.9 on 2021-12-25 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jirani', '0005_rename_description_business_descriptions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='descriptions',
            new_name='description',
        ),
    ]
