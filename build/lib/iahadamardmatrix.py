# -*- encoding: utf-8 -*-
# Module iahadamardmatrixfrom numpy import *

def iahadamardmatrix(N):
    from iaerror import iaerror
    from iameshgrid import iameshgrid

    def bitsum(x):
        s = 0 * x
        while x.any():
            s += x & 1
            x >>= 1
        return s

    n = floor(log(N)/log(2))

    if 2**n != N:
       iaerror('error: size '+str(N)+' is not multiple of power of 2')
       return -1

    u, x = iameshgrid(range(N), range(N))

    A = ((-1)**(bitsum(x & u)))/sqrt(N)
    return A

