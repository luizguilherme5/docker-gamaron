# Generated by Django 2.1.3 on 2018-11-13 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itens', '0001_initial'),
        ('users', '0003_auto_20181014_1220'),
        ('quests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserPlayer')),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('reward_xp', models.IntegerField()),
                ('reward_score', models.IntegerField()),
                ('time_beg', models.DateTimeField()),
                ('time_end', models.DateTimeField()),
                ('url', models.URLField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UserPlayer')),
                ('reward_iten', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='itens.Iten')),
            ],
        ),
        migrations.RemoveField(
            model_name='quests',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='quests',
            name='reward_iten',
        ),
        migrations.DeleteModel(
            name='Quests',
        ),
        migrations.AddField(
            model_name='journal',
            name='quest',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quests.Quest'),
        ),
    ]
