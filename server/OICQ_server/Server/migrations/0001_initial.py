# Generated by Django 3.0.5 on 2021-01-03 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SDPC_userdetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('c_perno', models.CharField(max_length=10, unique=True)),
                ('c_username', models.CharField(max_length=10)),
                ('c_phone', models.CharField(max_length=14)),
                ('c_gender', models.CharField(max_length=3)),
                ('c_email', models.CharField(blank=True, max_length=30)),
                ('c_address', models.CharField(blank=True, max_length=50)),
                ('c_sig', models.CharField(blank=True, max_length=100)),
                ('c_profile', models.ImageField(blank=True, upload_to='')),
                ('c_brief', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SDPC_login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=65)),
                ('laslogin', models.DateTimeField()),
                ('flag', models.BooleanField()),
                ('register_time', models.DateField()),
                ('useraccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Server.SDPC_userdetail', to_field='c_perno')),
            ],
        ),
        migrations.CreateModel(
            name='SDPC_addrbook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('friend_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Server.SDPC_userdetail', to_field='c_perno')),
                ('useraccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='self', to='Server.SDPC_userdetail', to_field='c_perno')),
            ],
        ),
    ]