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
    try:
        local("mkdir -p versions")
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(now)
        local("tar -cvzf {} web_static".format(archive_name)
        return archive_name
    except:
        return None

