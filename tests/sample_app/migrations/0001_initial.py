# Generated by Django 4.0.6 on 2022-08-30 07:20

from django.db import migrations, models
import django_pydantic_field.fields
import tests.sample_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta', django_pydantic_field.fields.PydanticSchemaField(config=None, default=(('type', tests.sample_app.models.BuildingTypes['FRAME']),), schema=tests.sample_app.models.BuildingMeta)),
            ],
        ),
    ]
