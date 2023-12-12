#!/usr/bin/python3

"""
script generates a .tgz archive from contents of web_static dir
"""
from datetime import datetime
from fabric.api import *
from fabric.operations import run, put
import os

env.hosts = ['52.205.85.168', '52.91.157.43']
#env.user = 'ubuntu'
#env.privkey = '~/.ssh/school'

def do_deploy(archive_path):
    """
    distributes archives to web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        arch_name = archive_path.split("/")[-1]
        dir_name = arch_name.split(".")[0]
        dir_path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(dir_path))
        run("tar -xzf /tmp/{} -C {}".format(arch_name, dir_path))
        run("rm -rf /tmp/{}".format(arch_name))
        run("sudo mv {}web_static/* {}".format(dir_path, dir_path))
        run("rm -rf {}{}/web_static".format(dir_path, dir_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(dir_path, dir_name))
        return True
    except Exception:
        return False
