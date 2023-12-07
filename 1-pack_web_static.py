#!/usr/bin/python3

"""
script generates a .tgz archive from contents of web_static dir
"""
from datetime import datetime
from fabric.api import local

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

if __name__ == "__main__":
    do_pack()
