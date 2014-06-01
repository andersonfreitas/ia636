# -*- encoding: utf-8 -*-
# Module iatcrgb2ind
from numpy import *

def iatcrgb2ind(f):
    from iaunique import iaunique

    f = asarray(f)
    r, g, b = f[0,:,:], f[1,:,:], f[2,:,:]
    c = r + 256*g + 256*256*b

    (t,i,fi) = iaunique(c)

    siz = len(t)
    rt = reshape(map(lambda k:int(k%256), t), (siz,1))
    gt = reshape(map(lambda k:int((k%(256*256))/256.), t), (siz,1))
    bt = reshape(map(lambda k:int(k), t/(256*256.)), (siz,1))

    cm = concatenate((rt, gt, bt), axis=1)
    fi = reshape(fi, (f.shape[1], f.shape[2]))
    return fi,cm

