#!/usr/bin/python3

from time import strftime
from fabric.api import local
from datetime import date

def do_pack():
    """ generating archs for of webstatic """
    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
