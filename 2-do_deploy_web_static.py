#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to web servers, using the function do_deploy"""

from fabric.api import env, put, run
import os

env.hosts = ["34.239.255.114", "3.83.253.172"]


def do_deploy(archive_path):
    """deploys web_static archive to remote servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[1]
        archive_name_2 = archive_name.split(".")[0]
        target = f"/data/web_static/releases/{archive_name_2}"
        link_name = "/data/web_static/current"

        put(archive_path, "/tmp/", use_sudo=True)
        run(f"tar -xvzf /tmp/{archive_name} -C /data/web_static/releases/")
        run(f"mv /data/web_static/releases/web_static {target}")
        run(f"rm -rf /tmp/{archive_name}")
        run(f"rm {link_name}")
        run(f"ln -sf {target} {link_name}")
        return True
    except Exception:
        return False
