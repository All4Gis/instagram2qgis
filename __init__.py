# -*- coding: utf-8 -*-
import sys

# try:
#     sys.path.append("C:/eclipse/plugins/org.python.pydev_4.3.0.201508182223/pysrc")
# except:
#     pass

def classFactory(iface):
    from Insta2QgisTool import Insta2QgisTool
    return Insta2QgisTool(iface)
