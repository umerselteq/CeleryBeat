# Generated by Django 4.2 on 2024-08-27 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('restored_at', models.DateTimeField(blank=True, null=True)),
                ('transaction_id', models.UUIDField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('parentId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childCandidates', to='my_celery_app.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('restored_at', models.DateTimeField(blank=True, null=True)),
                ('transaction_id', models.UUIDField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('review pending', 'Review Pending'), ('registered', 'Registered'), ('completed', 'Completed'), ('pending', 'Pending'), ('suspended', 'Suspended'), ('applied', 'Applied'), ('flow assigned', 'Flow Assigned')], default='registered', max_length=20)),
                ('candidateId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='my_celery_app.candidate')),
            ],
        ),
    ]
