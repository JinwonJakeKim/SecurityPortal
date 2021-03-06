# Generated by Django 3.1.3 on 2021-09-27 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0010_auto_20210926_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide_answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='model_guide',
            name='imgfile',
        ),
        migrations.RemoveField(
            model_name='model_regulation',
            name='imgfile',
        ),
        migrations.RemoveField(
            model_name='model_sktl_policy',
            name='imgfile',
        ),
        migrations.RemoveField(
            model_name='model_trend',
            name='imgfile',
        ),
        migrations.RemoveField(
            model_name='regulation_answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='sktl_policy_answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='trend_answer',
            name='question',
        ),
        migrations.AddField(
            model_name='guide_answer',
            name='guide',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pybo.model_guide'),
        ),
        migrations.AddField(
            model_name='regulation_answer',
            name='regulation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pybo.model_regulation'),
        ),
        migrations.AddField(
            model_name='sktl_policy_answer',
            name='SKTL_policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pybo.model_sktl_policy'),
        ),
        migrations.AddField(
            model_name='trend_answer',
            name='trend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pybo.model_trend'),
        ),
    ]
