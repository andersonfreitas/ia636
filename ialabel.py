# -*- encoding: utf-8 -*-
# Module ialabelfrom numpy import *

def ialabel(f):
    from iaind2sub import iaind2sub
    from iarec import iarec

    faux = 1*f
    g    = zeros(faux.shape, int)
    gaux = g.copy
    i = flatnonzero(faux)
    k = 1
    while len(i):
        aux = iaind2sub(faux.shape, i[0])
        gaux = iarec(faux, (aux[0],aux[1]))
        faux = faux - gaux
        g += k*gaux
        k += 1
        i = flatnonzero(faux)
    return g

