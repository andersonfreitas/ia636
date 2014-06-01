# -*- encoding: utf-8 -*-
# Module iafftshiftfrom numpy import *

def iafftshift(f):
    from ia636 import iaptrans

    f = asarray(f)

    return iaptrans(f, array(f.shape)/2)

