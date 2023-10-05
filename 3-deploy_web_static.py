#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your web servers"""

from datetime import datetime
from fabric.api import env, local, put, run
import os

env.hosts = ["34.239.255.114", "3.83.253.172"]


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


def deploy():
    """calls do_pack and do_deploy to
    create and distribute an archive to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
