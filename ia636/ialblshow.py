# -*- encoding: utf-8 -*-
# Module ialblshowfrom numpy import *
from numpy.random import rand

def ialblshow(f):
    from iaapplylut import iaapplylut

    nblobs = max(ravel(f))
    r = floor(0.5 + 255*rand(nblobs, 1))
    g = floor(0.5 + 255*rand(nblobs, 1))
    b = floor(0.5 + 255*rand(nblobs, 1))
    ct = concatenate((r,g,b), 1)
    ct = concatenate(([[0,0,0]], ct))

    g = iaapplylut(f, ct)
    return g

