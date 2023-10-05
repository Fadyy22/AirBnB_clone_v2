#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
from the contents of the web_static folder of AirBnB Clone repo"""

from datetime import datetime
import os
from fabric.api import local


def do_pack():
    """packs web_static folder to .trg"""
    date = datetime.now()
    path = "./web_static"
    archive = f"web_static_{date.strftime('%Y%m%d%H%M%S')}"

    try:
        if not os.path.exists("./versions"):
            local("mkdir versions")
        local(f"tar -czvf versions/{archive}.tgz {path}")
        return f"versions/{archive}.tgz"
    except Exception:
        return None
