# Generated by Django 3.1.7 on 2021-03-27 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_auto_20210327_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentCrm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment_text', models.TextField(verbose_name='Текст комментария')),
                ('coment_dt', models.DateTimeField(auto_now=True, verbose_name='Время создания')),
                ('coment_binding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.order', verbose_name='Заявка')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
