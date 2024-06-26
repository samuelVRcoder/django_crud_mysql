from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=10)),
                ('ename', models.CharField(max_length=50)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
