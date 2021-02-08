#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "P2PLending.envs.local")

    from django.core.management import execute_from_command_line
    # from P2PLending.lending import #TODO fit model here
    import P2PLending.money.currencies
    execute_from_command_line(sys.argv)
