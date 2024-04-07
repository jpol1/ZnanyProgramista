# Generated by Django 4.2.11 on 2024-04-07 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgrammerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wage_min', models.PositiveIntegerField()),
                ('wage_max', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=5000)),
                ('experience', models.CharField(choices=[('Mid', 'Mid'), ('Junior', 'Junior'), ('Senior', 'Senior')], max_length=100)),
                ('portfolio', models.URLField(max_length=1000)),
                ('programming_languages', multiselectfield.db.fields.MultiSelectField(choices=[('JavaScript', 'JavaScript'), ('Python', 'Python'), ('Java', 'Java'), ('C', 'C'), ('C++', 'C++'), ('C#', 'C#'), ('R', 'R'), ('PHP', 'PHP'), ('SQL', 'SQL'), ('RUST', 'RUST'), ('Kotlin', 'Kotlin'), ('HTML', 'HTML'), ('CSS', 'CSS'), ('TypeScript', 'TypeScript'), ('Scala', 'Scala'), ('SWIFT', 'SWIFT')], max_length=500)),
                ('tech_stack', multiselectfield.db.fields.MultiSelectField(choices=[('Django', 'Django'), ('Celery', 'Celery'), ('Flask', 'Flask'), ('FastAPI', 'FastAPI'), ('Databases', 'Databases'), ('Docker', 'Docker'), ('Git | GitHub', 'Git | GitHub'), ('Node.js', 'Node.js'), ('React', 'React'), ('Symphony', 'Symphony'), ('Ruby on Rails', 'Ruby on Rails')], max_length=500)),
                ('phone', models.CharField(max_length=11, null=True, unique=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='programmer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('programmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='programmers.programmerprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_given', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
