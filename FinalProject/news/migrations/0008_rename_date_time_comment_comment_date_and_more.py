# Generated by Django 4.1.2 on 2022-10-21 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_post_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='date_time',
            new_name='comment_date',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='comment_post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='rating',
            new_name='comment_rating',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='text_comment',
            new_name='comment_text',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='comment_user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='rating',
            new_name='post_rating',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='time_in',
            new_name='posting_time',
        ),
        migrations.AlterField(
            model_name='post',
            name='choice',
            field=models.CharField(choices=[('news', 'Новости'), ('articles', 'Статьи')], default='articles', max_length=10),
        ),
    ]
