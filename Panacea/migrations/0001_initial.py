# Generated by Django 2.2b1 on 2019-10-31 15:58

import Panacea.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import localflavor.us.models
import phonenumber_field.modelfields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ending_balance_categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ending_balance_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='expenses_source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specific_expense_source', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80)),
                ('address_line_1', models.CharField(blank=True, max_length=50)),
                ('address_line_2', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2)),
                ('zip_code', localflavor.us.models.USZipCodeField(blank=True, max_length=10)),
                ('classification', models.CharField(blank=True, choices=[('Urban', 'Urban'), ('Small Urban', 'Small Urban'), ('Rural', 'Rural')], max_length=50, null=True)),
                ('vanpool_program', models.BooleanField(blank=True, default=True, null=True)),
                ('vanshare_program', models.BooleanField(blank=True, null=True)),
                ('vanpool_expansion', models.BooleanField(blank=True, null=True)),
                ('in_jblm_area', models.BooleanField(blank=True, null=True)),
                ('in_puget_sound_area', models.BooleanField(blank=True, null=True)),
                ('summary_organization_classifications', models.CharField(blank=True, choices=[('Community provider', 'Community provider'), ('Ferry', 'Ferry'), ('Intercity bus', 'Intercity bus'), ('Medicaid broker', 'Medicaid broker'), ('Monorail', 'Monorail'), ('Transit', 'Transit'), ('Tribe', 'Tribe')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='revenue_source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specific_revenue_source', models.CharField(blank=True, max_length=120, null=True)),
                ('order_in_summary', models.IntegerField(blank=True, null=True)),
                ('government_type', models.CharField(blank=True, choices=[('Federal', 'Federal'), ('State', 'State'), ('Local', 'Local'), ('Other', 'Other')], max_length=100, null=True)),
                ('funding_type', models.CharField(blank=True, choices=[('Capital', 'Capital'), ('Operating', 'Operating')], max_length=30, null=True)),
                ('agency_funding_classification', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='rollup_mode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollup_mode', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='transit_metrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='transit_mode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(blank=True, max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='custom_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('random_field', models.CharField(blank=True, max_length=80)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', Panacea.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='vanpool_expansion_analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vanpools_in_service_at_time_of_award', models.IntegerField(blank=True, null=True)),
                ('date_of_award', models.DateField(blank=True, null=True)),
                ('expansion_vans_awarded', models.IntegerField(blank=True, null=True)),
                ('latest_vehicle_acceptance', models.DateField(blank=True, null=True)),
                ('extension_granted', models.BooleanField(null=True)),
                ('vanpool_goal_met', models.BooleanField(null=True)),
                ('expired', models.BooleanField(null=True)),
                ('notes', models.TextField(null=True)),
                ('award_biennium', models.CharField(blank=True, choices=[('11-13', '11-13'), ('13-15', '13-15'), ('15-17', '15-17'), ('17-19', '17-19'), ('19-21', '19-21'), ('21-23', '21-23'), ('23-25', '23-25'), ('25-27', '25-27')], max_length=50, null=True)),
                ('expansion_goal', models.IntegerField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('service_goal_met_date', models.DateField(blank=True, null=True)),
                ('max_vanpool_numbers', models.IntegerField(blank=True, null=True)),
                ('max_vanpool_date', models.DateField(blank=True, null=True)),
                ('latest_vanpool_number', models.IntegerField(blank=True, null=True)),
                ('latest_report_date', models.DateField(blank=True, null=True)),
                ('months_remaining', models.CharField(blank=True, max_length=20, null=True)),
                ('organization_name', models.CharField(blank=True, max_length=100, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Panacea.organization')),
            ],
        ),
        migrations.CreateModel(
            name='SummaryTransitData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('administration_of_mode', models.CharField(choices=[('Direct Operated', 'Direct Operated'), ('Purchased', 'Purchased')], max_length=80)),
                ('metric_value', models.FloatField()),
                ('comments', models.TextField(null=True)),
                ('metric', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Panacea.transit_metrics')),
                ('mode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Panacea.transit_mode')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Panacea.organization')),
                ('report_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('rollup_mode', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Panacea.rollup_mode')),
            ],
        ),
        migrations.CreateModel(
            name='SummaryRevenues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('specific_revenue_value', models.FloatField(blank=True, null=True)),
                ('comments', models.TextField(null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Panacea.organization')),
                ('report_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('specific_revenue_source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Panacea.revenue_source')),
            ],
        ),
        migrations.CreateModel(
            name='SummaryExpenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('specific_expense_value', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Panacea.organization')),
                ('report_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('specific_expense_source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Panacea.expenses_source')),
            ],
        ),
        migrations.CreateModel(
            name='subfundRevenues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subfund_specification', models.TextField(null=True)),
                ('specific_revenue_value', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Panacea.SummaryRevenues')),
            ],
        ),
        migrations.CreateModel(
            name='subfundExpenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subfund_specification', models.TextField(null=True)),
                ('specific_expense_value', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Panacea.SummaryExpenses')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceOffered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administration_of_mode', models.CharField(blank=True, choices=[('Direct Operated', 'Direct Operated'), ('Purchased', 'Purchased')], max_length=80)),
                ('mode', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Panacea.transit_mode')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Panacea.organization')),
            ],
        ),
        migrations.CreateModel(
            name='ReportType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('report_frequency', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Yearly', 'Yearly'), ('Other', 'Other')], default='Yearly', max_length=50)),
                ('due_date', models.DateField()),
                ('report_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_submitted', models.BooleanField(default=False)),
                ('profile_complete', models.BooleanField(default=False)),
                ('telephone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('job_title', models.CharField(blank=True, max_length=100)),
                ('address_line_1', models.CharField(blank=True, max_length=50)),
                ('address_line_2', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', localflavor.us.models.USStateField(blank=True, max_length=2)),
                ('zip_code', localflavor.us.models.USZipCodeField(blank=True, max_length=10)),
                ('active_permissions_request', models.BooleanField(blank=True, null=True)),
                ('custom_user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Panacea.organization')),
                ('reports_on', models.ManyToManyField(blank=True, to='Panacea.ReportType')),
            ],
        ),
        migrations.CreateModel(
            name='Historicalvanpool_report',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('report_year', models.IntegerField()),
                ('report_month', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('report_date', models.DateTimeField(default=None, null=True)),
                ('update_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('vanshare_groups_in_operation', models.IntegerField(blank=True, null=True)),
                ('vanshare_group_starts', models.IntegerField(blank=True, null=True)),
                ('vanshare_group_folds', models.IntegerField(blank=True, null=True)),
                ('vanshare_passenger_trips', models.IntegerField(blank=True, null=True)),
                ('vanshare_miles_traveled', models.FloatField(blank=True, null=True)),
                ('vanpool_groups_in_operation', models.IntegerField(blank=True, null=True)),
                ('vanpool_group_starts', models.IntegerField(blank=True, null=True)),
                ('vanpool_group_folds', models.IntegerField(blank=True, null=True)),
                ('vans_available', models.IntegerField(blank=True, null=True)),
                ('loaner_spare_vans_in_fleet', models.IntegerField(blank=True, null=True)),
                ('vanpool_passenger_trips', models.IntegerField(blank=True, null=True)),
                ('vanpool_miles_traveled', models.FloatField(blank=True, null=True)),
                ('average_riders_per_van', models.FloatField(blank=True, null=True)),
                ('average_round_trip_miles', models.FloatField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.organization')),
                ('report_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('report_type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.ReportType')),
            ],
            options={
                'verbose_name': 'historical vanpool_report',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Historicalvanpool_expansion_analysis',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('vanpools_in_service_at_time_of_award', models.IntegerField(blank=True, null=True)),
                ('date_of_award', models.DateField(blank=True, null=True)),
                ('expansion_vans_awarded', models.IntegerField(blank=True, null=True)),
                ('latest_vehicle_acceptance', models.DateField(blank=True, null=True)),
                ('extension_granted', models.BooleanField(null=True)),
                ('vanpool_goal_met', models.BooleanField(null=True)),
                ('expired', models.BooleanField(null=True)),
                ('notes', models.TextField(null=True)),
                ('award_biennium', models.CharField(blank=True, choices=[('11-13', '11-13'), ('13-15', '13-15'), ('15-17', '15-17'), ('17-19', '17-19'), ('19-21', '19-21'), ('21-23', '21-23'), ('23-25', '23-25'), ('25-27', '25-27')], max_length=50, null=True)),
                ('expansion_goal', models.IntegerField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('service_goal_met_date', models.DateField(blank=True, null=True)),
                ('max_vanpool_numbers', models.IntegerField(blank=True, null=True)),
                ('max_vanpool_date', models.DateField(blank=True, null=True)),
                ('latest_vanpool_number', models.IntegerField(blank=True, null=True)),
                ('latest_report_date', models.DateField(blank=True, null=True)),
                ('months_remaining', models.CharField(blank=True, max_length=20, null=True)),
                ('organization_name', models.CharField(blank=True, max_length=100, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.organization')),
            ],
            options={
                'verbose_name': 'historical vanpool_expansion_analysis',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSummaryTransitData',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('administration_of_mode', models.CharField(choices=[('Direct Operated', 'Direct Operated'), ('Purchased', 'Purchased')], max_length=80)),
                ('metric_value', models.FloatField()),
                ('comments', models.TextField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('metric', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.transit_metrics')),
                ('mode', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.transit_mode')),
                ('organization', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.organization')),
                ('report_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('rollup_mode', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.rollup_mode')),
            ],
            options={
                'verbose_name': 'historical summary transit data',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSummaryRevenues',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('specific_revenue_value', models.FloatField(blank=True, null=True)),
                ('comments', models.TextField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.organization')),
                ('report_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('specific_revenue_source', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.revenue_source')),
            ],
            options={
                'verbose_name': 'historical summary revenues',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSummaryExpenses',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('specific_expense_value', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.organization')),
                ('report_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('specific_expense_source', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.expenses_source')),
            ],
            options={
                'verbose_name': 'historical summary expenses',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Historicalending_balances',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('ending_balance_value', models.FloatField()),
                ('year', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('ending_balance_category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.ending_balance_categories')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.organization')),
                ('report_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical ending_balances',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Historicaldepreciation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('depreciation', models.IntegerField(null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Panacea.organization')),
                ('report_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical depreciation',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='ending_balances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ending_balance_value', models.FloatField()),
                ('year', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('ending_balance_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='Panacea.ending_balance_categories')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Panacea.organization')),
                ('report_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='depreciation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depreciation', models.IntegerField(null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Panacea.organization')),
                ('report_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cover_sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('executive_officer_first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('executive_officer_last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('executive_officer_title', models.CharField(blank=True, max_length=50, null=True)),
                ('service_website_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Service website URL')),
                ('service_area_description', models.CharField(blank=True, max_length=500, null=True)),
                ('congressional_districts', models.CharField(blank=True, max_length=100, null=True)),
                ('legislative_districts', models.CharField(blank=True, max_length=100, null=True)),
                ('type_of_government', models.CharField(blank=True, max_length=100, null=True)),
                ('governing_body', models.TextField(blank=True, null=True)),
                ('tax_rate_description', models.CharField(blank=True, max_length=250, null=True)),
                ('transit_development_plan_url', models.CharField(blank=True, max_length=250, null=True, verbose_name='Transit development plan URL')),
                ('intermodal_connections', models.TextField(blank=True, null=True)),
                ('fares_description', models.TextField(blank=True, null=True)),
                ('service_and_eligibility', models.TextField(blank=True, null=True, verbose_name='Service and eligibility description')),
                ('current_operations', models.TextField(blank=True, null=True)),
                ('revenue_service_vehicles', models.TextField(blank=True, null=True, verbose_name='Revenue service vehicles')),
                ('days_of_service', models.CharField(blank=True, max_length=250, null=True, verbose_name='Days of service')),
                ('monorail_ownership', models.CharField(blank=True, max_length=250, null=True)),
                ('community_planning_region', models.CharField(blank=True, max_length=50, null=True)),
                ('organization_logo', models.BinaryField(blank=True, editable=True, null=True)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Panacea.organization')),
            ],
        ),
        migrations.CreateModel(
            name='vanpool_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_year', models.IntegerField()),
                ('report_month', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('report_date', models.DateTimeField(default=None, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('vanshare_groups_in_operation', models.IntegerField(blank=True, null=True)),
                ('vanshare_group_starts', models.IntegerField(blank=True, null=True)),
                ('vanshare_group_folds', models.IntegerField(blank=True, null=True)),
                ('vanshare_passenger_trips', models.IntegerField(blank=True, null=True)),
                ('vanshare_miles_traveled', models.FloatField(blank=True, null=True)),
                ('vanpool_groups_in_operation', models.IntegerField(blank=True, null=True)),
                ('vanpool_group_starts', models.IntegerField(blank=True, null=True)),
                ('vanpool_group_folds', models.IntegerField(blank=True, null=True)),
                ('vans_available', models.IntegerField(blank=True, null=True)),
                ('loaner_spare_vans_in_fleet', models.IntegerField(blank=True, null=True)),
                ('vanpool_passenger_trips', models.IntegerField(blank=True, null=True)),
                ('vanpool_miles_traveled', models.FloatField(blank=True, null=True)),
                ('average_riders_per_van', models.FloatField(blank=True, null=True)),
                ('average_round_trip_miles', models.FloatField(blank=True, null=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Panacea.organization')),
                ('report_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('report_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Panacea.ReportType')),
            ],
            options={
                'unique_together': {('organization', 'report_year', 'report_month')},
            },
        ),
        migrations.AddConstraint(
            model_name='summaryexpenses',
            constraint=models.UniqueConstraint(fields=('organization', 'year', 'specific_expense_source'), name='unique_source_report'),
        ),
    ]
