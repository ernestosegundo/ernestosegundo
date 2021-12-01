# Generated by Django 3.2.9 on 2021-12-01 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211130_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contenidopost',
            name='contenido',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cuerpo',
        ),
        migrations.AddField(
            model_name='contenidopost',
            name='cuerpo',
            field=models.ForeignKey(default=1980, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='blog.post'),
            preserve_default=False,
        ),
    ]
