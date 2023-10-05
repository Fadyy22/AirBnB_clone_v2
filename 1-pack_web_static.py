#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder of AirBnB Clone repo"""

import datetime
from fabric.api import local


def do_pack():
    """packs web_static folder to .trg"""
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day
    h = datetime.datetime.now().hour
    mi = datetime.datetime.now().minute
    s = datetime.datetime.now().second
    path = "./web_static"
    archive = f"web_static_{y}{m}{d}{h}{mi}{s}"

    local("mkdir versions")
    local(f"tar -czvf versions/{archive}.tgz {path}")
