# Generated by Django 4.1.7 on 2023-07-24 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournaments', '0010_alter_round_draw_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('permissions', utils.fields.ChoiceArrayField(base_field=models.CharField(choices=[('view.adjudicatorteamconflict', 'view adjudicator-team conflicts'), ('edit.adjudicatorteamconflict', 'edit adjudicator-team conflicts'), ('view.adjudicatoradjudicatorconflict', 'view adjudicator-adjudicator conflicts'), ('edit.adjudicatoradjudicatorconflict', 'edit adjudicator-adjudicator conflicts'), ('view.adjudicatorinstitutionconflict', 'view adjudicator-institution conflicts'), ('edit.adjudicatorinstitutionconflict', 'edit adjudicator-institution conflicts'), ('view.teaminstitutionconflict', 'view team-institution conflicts'), ('edit.teaminstitutionconflict', 'edit team-institution conflicts'), ('view.actionlogentry', 'view action log entries'), ('view.team', 'view teams'), ('add.team', 'add teams'), ('view.roundavailability.team', 'view round availabilities for teams'), ('view.roundavailability.adjudicator', 'view round availabilities for adjudicators'), ('view.roundavailability.venue', 'view round availabilities for rooms'), ('edit.roundavailability.team', 'edit round availabilities for teams'), ('edit.roundavailability.adjudicator', 'edit round availabilities for adjudicators'), ('edit.roundavailability.venue', 'edit round availabilities for rooms'), ('view.debate', 'view debates (draw)'), ('view.debate.admin', 'view debates (detailed draw)'), ('generate.debate', 'generate debates (draw)'), ('edit.debateteam', 'edit debate teams (pairings)'), ('view.debateadjudicator', 'view debate adjudicators (allocations)'), ('edit.debateadjudicator', 'edit debate adjudicators (allocations)'), ('view.ballotsubmission.new', 'view confirmed ballots'), ('edit.ballotsubmission.old', 'edit non-confirmed ballots'), ('view.ballotsubmission', 'view any ballot'), ('edit.ballotsubmission', 'edit any ballot'), ('add.ballotsubmission', 'create ballots'), ('mark.ballotsubmission', 'confirm/discard any ballot'), ('mark.ballotsubmission.others', "confirm/discard others' ballots"), ('view.ballotsubmission.graph', 'view ballot graph'), ('view.tournamentpreferencemodel', 'view tournament configuration'), ('edit.tournamentpreferencemodel', 'edit tournament configuration')], max_length=50), blank=True, default=list, size=None, verbose_name='permissions')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament', verbose_name='tournament')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
                'unique_together': {('name', 'tournament')},
            },
        ),
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('view.adjudicatorteamconflict', 'view adjudicator-team conflicts'), ('edit.adjudicatorteamconflict', 'edit adjudicator-team conflicts'), ('view.adjudicatoradjudicatorconflict', 'view adjudicator-adjudicator conflicts'), ('edit.adjudicatoradjudicatorconflict', 'edit adjudicator-adjudicator conflicts'), ('view.adjudicatorinstitutionconflict', 'view adjudicator-institution conflicts'), ('edit.adjudicatorinstitutionconflict', 'edit adjudicator-institution conflicts'), ('view.teaminstitutionconflict', 'view team-institution conflicts'), ('edit.teaminstitutionconflict', 'edit team-institution conflicts'), ('view.actionlogentry', 'view action log entries'), ('view.team', 'view teams'), ('add.team', 'add teams'), ('view.roundavailability.team', 'view round availabilities for teams'), ('view.roundavailability.adjudicator', 'view round availabilities for adjudicators'), ('view.roundavailability.venue', 'view round availabilities for rooms'), ('edit.roundavailability.team', 'edit round availabilities for teams'), ('edit.roundavailability.adjudicator', 'edit round availabilities for adjudicators'), ('edit.roundavailability.venue', 'edit round availabilities for rooms'), ('view.debate', 'view debates (draw)'), ('view.debate.admin', 'view debates (detailed draw)'), ('generate.debate', 'generate debates (draw)'), ('edit.debateteam', 'edit debate teams (pairings)'), ('view.debateadjudicator', 'view debate adjudicators (allocations)'), ('edit.debateadjudicator', 'edit debate adjudicators (allocations)'), ('view.ballotsubmission.new', 'view confirmed ballots'), ('edit.ballotsubmission.old', 'edit non-confirmed ballots'), ('view.ballotsubmission', 'view any ballot'), ('edit.ballotsubmission', 'edit any ballot'), ('add.ballotsubmission', 'create ballots'), ('mark.ballotsubmission', 'confirm/discard any ballot'), ('mark.ballotsubmission.others', "confirm/discard others' ballots"), ('view.ballotsubmission.graph', 'view ballot graph'), ('view.tournamentpreferencemodel', 'view tournament configuration'), ('edit.tournamentpreferencemodel', 'edit tournament configuration')], max_length=50, verbose_name='permission')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.tournament', verbose_name='tournament')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'user permission',
                'verbose_name_plural': 'user permissions',
                'unique_together': {('user', 'permission', 'tournament')},
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.group', verbose_name='group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'group membership',
                'verbose_name_plural': 'group memberships',
                'unique_together': {('user', 'group')},
            },
        ),
    ]