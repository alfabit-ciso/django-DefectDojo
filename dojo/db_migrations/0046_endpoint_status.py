# Generated by Django 2.2.14 on 2020-07-01 22:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import dojo.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dojo', '0045_slack_help_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endpoint',
            old_name='remediated',
            new_name='mitigated',
        ),
        migrations.CreateModel(
            name='Endpoint_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=dojo.models.get_current_date)),
                ('last_modified', models.DateTimeField(default=dojo.models.get_current_datetime, editable=False, null=True)),
                ('mitigated', models.BooleanField(blank=True, default=False)),
                ('mitigated_time', models.DateTimeField(blank=True, editable=False, null=True)),
                ('false_positive', models.BooleanField(blank=True, default=False)),
                ('out_of_scope', models.BooleanField(blank=True, default=False)),
                ('risk_accepted', models.BooleanField(blank=True, default=False)),
                ('endpoint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_endpoint', to='dojo.Endpoint')),
                ('finding', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='status_finding', to='dojo.Finding')),
                ('mitigated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='endpoint',
            name='endpoint_status',
            field=models.ManyToManyField(blank=True, related_name='endpoint_endpoint_status', to='dojo.Endpoint_Status'),
        ),
        migrations.AddField(
            model_name='finding',
            name='endpoint_status',
            field=models.ManyToManyField(blank=True, related_name='finding_endpoint_status', to='dojo.Endpoint_Status'),
        ),
    ]