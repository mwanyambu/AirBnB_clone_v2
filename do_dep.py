#!/usr/bin/python3

"""
script generates a .tgz archive from contents of web_static dir
"""
from datetime import datetime
from fabric.api import *
from fabric.operations import run, put
import os

def do_pack():
    """
    creates a .tgz archive
    """
    try:
        local("mkdir -p versions")
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(now)
        local("tar -cvzf {} web_static".format(archive_name))
        if os.path.exists(archive_name):
            return archive_name
        else:
            return None
    except Exception:
        return None

env.hosts = ['52.205.85.168', '52.91.157.43']
env.user = 'ubuntu'
env.privkey = '~/.ssh/school'

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
        run("tar -xzf /tmp/{} -C {}".format(arch_name, dir_path))
        run("rm -rf /tmp/{}".format(arch_name))
        run("mv {}web_static/* {}".format(dir_path, dir_path))
        run("rm -rf {}web_static".format(dir_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dir_path))
        success = True
    
    except Exception:
        success = False
    return success
