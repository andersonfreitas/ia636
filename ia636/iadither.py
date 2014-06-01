# -*- encoding: utf-8 -*-
# Module iadither
from numpy import *

def iadither(f, n):
    from ianormalize import ianormalize

    D = 1.*array([[0,2],[3,1]])
    d = 1*D
    k = log(n/2.)/log(2.)
    for i in range(k):
        u = ones(D.shape)
        d1 = 4*D + d[0,0]*u
        d2 = 4*D + d[0,1]*u
        d3 = 4*D + d[1,0]*u
        d4 = 4*D + d[1,1]*u
        D = concatenate((concatenate((d1,d2),1), concatenate((d3,d4),1)))
    D = 255*abs(D/max(ravel(D)))
    g = tile(D.astype('b'), f.shape)
    g = ianormalize(f,[0,255]) >= g
    return g

