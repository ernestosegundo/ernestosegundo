# Generated by Django 3.2.9 on 2021-12-01 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContenidoPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_contenido', models.CharField(choices=[('T', 'Texto'), ('I', 'Imagen')], max_length=1)),
                ('contenido', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='contenido',
        ),
        migrations.AddField(
            model_name='post',
            name='cuerpo',
            field=models.ForeignKey(default=1980, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='blog.contenidopost'),
            preserve_default=False,
        ),
    ]
