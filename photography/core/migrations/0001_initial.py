# Generated by Django 2.0.5 on 2018-05-19 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_500px', models.URLField(blank=True, help_text='Your 500px page URL')),
                ('_500px_Text', models.TextField(blank=True, help_text='If set this text will show instead of the Font Awesome logo')),
                ('facebook', models.URLField(blank=True, help_text='Your Facebook page URL')),
                ('facebook_Text', models.TextField(blank=True, help_text='If set this text will show instead of the Font Awesome logo')),
                ('instagram', models.URLField(blank=True, help_text='Your Instagram page URL')),
                ('instagram_Text', models.TextField(blank=True, help_text='If set this text will show instead of the Font Awesome logo')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Social Media Accounts',
            },
        ),
    ]
