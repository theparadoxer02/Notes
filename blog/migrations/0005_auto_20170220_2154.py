# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160828_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='picture',
            field=models.ImageField(upload_to=b'blog/media/%Y/%m/%d'),
        ),
    ]
