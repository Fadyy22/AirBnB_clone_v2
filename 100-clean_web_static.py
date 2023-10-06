#!/usr/bin/python3
"""Fabric script that deletes out-of-date archives"""

from fabric.api import local, run


def do_clean(number=0):
    """deletes out-of-date archives"""
    number = int(number)

    if number == 0 or number == 1:
        number = 2
    elif number == 2:
        number = 3

    cmd = f"ls -t | tail -n +{number} | xargs rm -rf"
    local(f"cd versions/ ; {cmd}")
    run(f"cd /data/web_static/releases/ ; {cmd} ")
