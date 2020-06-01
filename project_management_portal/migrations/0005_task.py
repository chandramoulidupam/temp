# Generated by Django 2.2.1 on 2020-05-29 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_management_portal', '0004_auto_20200528_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('issue_type', models.CharField(choices=[('Task', 'Task'), ('Bug', 'Bug'), ('Developer_Story', 'Developer_Story'), ('User_Story', 'User_Story'), ('Enhancement', 'Enhancement')], max_length=100)),
                ('assigned_to', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('project', models.ManyToManyField(to='project_management_portal.Project')),
                ('state_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_management_portal.State')),
            ],
        ),
    ]
