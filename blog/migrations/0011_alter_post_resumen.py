# Generated by Django 3.2.9 on 2021-12-02 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resumen',
            field=models.CharField(max_length=500),
        ),
    ]