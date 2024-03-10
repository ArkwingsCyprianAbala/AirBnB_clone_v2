#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *
import os


def do_pack():
    """
    making an archive on web_static folder
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    t_str = time.strftime('%Y%m%d%H%M%S')
    f_path = f"versions/web_static_{t_str}.tgz"
    f_size = os.path.getsize(f_path)
    print(f"web_static packed: {f_path} -> {f_size}Bytes")
    if create is not None:
        return archive
    else:
        return None
