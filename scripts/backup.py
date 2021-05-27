#!/usr/bin/env python

import subprocess
from django.apps import apps

for model in apps.get_models():
    model_str = f'{model._meta.app_label}.{model.__name__}.json'
    print(model_str)
    subprocess.call(['python', 'manage.py', 'dumpdata', '--indent', '2', '-o', f'{model_str}.json', model_str])
