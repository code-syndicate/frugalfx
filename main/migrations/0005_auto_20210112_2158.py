# Generated by Django 3.1.4 on 2021-01-12 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_withdrawalrequest_settled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='bank_acct_no',
            field=models.CharField(blank=True, max_length=25, verbose_name='Bank Account Number'),
        ),
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='bank_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='Bank Name'),
        ),
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='bank_swift',
            field=models.CharField(blank=True, max_length=16, verbose_name='Bank SWIFT'),
        ),
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='desc',
            field=models.TextField(verbose_name='Description '),
        ),
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='mode',
            field=models.CharField(choices=[('bank', 'bank'), ('wallet', 'wallet')], max_length=25, verbose_name='Payment Mode'),
        ),
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='settled',
            field=models.BooleanField(default=False, verbose_name='Paid'),
        ),
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='wallet_addr',
            field=models.CharField(blank=True, max_length=72, verbose_name='Wallet Address'),
        ),
        migrations.AlterField(
            model_name='withdrawalrequest',
            name='wallet_type',
            field=models.CharField(blank=True, choices=[('bitcoin', 'bitcoin'), ('eth', 'eth')], max_length=25, verbose_name='Wallet Type'),
        ),
        migrations.CreateModel(
            name='AuthPin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('generated_on', models.DateTimeField(auto_now_add=True)),
                ('used', models.BooleanField(default=False, editable=False)),
                ('is_invalid', models.BooleanField(default=False)),
                ('for_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pins', to=settings.AUTH_USER_MODEL)),
                ('withdraw_request', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='reqs', to='main.withdrawalrequest')),
            ],
        ),
    ]