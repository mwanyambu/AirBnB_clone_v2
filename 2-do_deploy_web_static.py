#!/usr/bin/python3

"""
script generates a .tgz archive from contents of web_static dir
"""
from datetime import datetime
from fabric.api import local
import os

def do_pack():
    """
    creates a .tgz archive
    """
    local("mkdir -p versions")
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(now)
    arch = local("tar -cvzf {} web_static".format(archive_name)
    if arch.return_code != 0:
        return None
    else:
        return arch

def do_deploy(archive_path):
    """
    distributes archives to web servers
    """
    if not os.path.exists(archive_path):
        return False

    arch_name = os.path.basename(archive_path)
    dir_name = arch_name.replace(".tgz", "")
    dir_path = "/data/web_static/releases/{}/".format(dir_name)
    success = False

    try:
        put(archive_path, "/tmp/{}".format(arch_name))
        run("mkdir -p {}".format(dir_path))
        run("tar -xzf /tmp/{}".format(arch_name, dir_path))
        run("rm -rf /tmp/{}".format(arch_name))
        run("mv {}web_static/* {}".format(dir_path, dir_path))
        run("rm -rf {}web_static".format(dir_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dir_path))
        success = True
    
    except Exception:
        success = False
    return success
