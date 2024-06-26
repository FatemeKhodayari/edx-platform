# Generated by Django 4.2.13 on 2024-05-13 19:22

import common.djangoapps.third_party_auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('third_party_auth', '0012_alter_ltiproviderconfig_site_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ltiproviderconfig',
            name='site',
            field=models.ForeignKey(default=common.djangoapps.third_party_auth.models._get_site_id_from_settings, help_text='The Site that this provider configuration belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='sites.site'),
        ),
        migrations.AlterField(
            model_name='oauth2providerconfig',
            name='site',
            field=models.ForeignKey(default=common.djangoapps.third_party_auth.models._get_site_id_from_settings, help_text='The Site that this provider configuration belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='sites.site'),
        ),
        migrations.AlterField(
            model_name='samlconfiguration',
            name='site',
            field=models.ForeignKey(default=common.djangoapps.third_party_auth.models._get_site_id_from_settings, help_text='The Site that this SAML configuration belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='sites.site'),
        ),
        migrations.AlterField(
            model_name='samlproviderconfig',
            name='site',
            field=models.ForeignKey(default=common.djangoapps.third_party_auth.models._get_site_id_from_settings, help_text='The Site that this provider configuration belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='sites.site'),
        ),
    ]
