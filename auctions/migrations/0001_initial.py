
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bidding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidder', models.CharField(blank=True, max_length=50, null=True)),
                ('bidprice', models.DecimalField(decimal_places=2, max_digits=15)),
                ('listingid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Closebid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productnames', models.CharField(max_length=20)),
                ('images', models.URLField(blank=True, null=True)),
                ('lister', models.CharField(blank=True, max_length=64, null=True)),
                ('bidder', models.CharField(blank=True, max_length=64, null=True)),
                ('listingid', models.IntegerField()),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('finalbid', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=64, null=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('comment', models.CharField(max_length=30)),
                ('listingid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productnames', models.CharField(max_length=20)),
                ('descriptions', models.TextField(max_length=500)),
                ('startingbids', models.DecimalField(decimal_places=2, max_digits=15)),
                ('images', models.URLField(blank=True, null=True)),
                ('category', models.CharField(blank=True, choices=[('МАШИНЫ', 'Cars'), ('КОСМЕТИКА', 'Makeup'), ('УСТРОЙСТВА', 'Devices'), ('ЗДОРОВЬЕ', 'Health'), ('СПОРТ', 'Sports'), ('РАЗВЛЕЧЕНИЯ', 'Entertainment')], max_length=50, null=True)),
                ('lister', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productnames', models.CharField(max_length=20)),
                ('images', models.URLField(blank=True, null=True)),
                ('finalbid', models.DecimalField(decimal_places=2, max_digits=15)),
                ('lister', models.CharField(blank=True, max_length=50, null=True)),
                ('watcher', models.CharField(blank=True, max_length=50, null=True)),
                ('listingid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
