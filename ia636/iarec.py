# -*- encoding: utf-8 -*-
# Module iarecfrom numpy import *

def iarec(f, seed):

    faux = f.copy()
    g = zeros_like(f)
    S = [seed,]
    while len(S):
        x, y = S.pop()
        if 0 <= x < faux.shape[0] and 0 <= y < faux.shape[1]:
            if faux[x,y]:
                faux[x,y], g[x,y] = False, True
                S.append((x+1, y  ))
                S.append((x-1, y  ))
                S.append((x  , y+1))
                S.append((x  , y-1))
    return g

