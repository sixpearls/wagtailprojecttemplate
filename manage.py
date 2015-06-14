#!/usr/bin/env python

import os
import sys
import local

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.%s"% local.ENVIRONMENT)
    execute_from_command_line(sys.argv)
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings")

    # from django.core.management import execute_from_command_line

    # execute_from_command_line(sys.argv)
