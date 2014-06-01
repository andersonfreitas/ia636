# -*- encoding: utf-8 -*-
# Module iacosimport numpy as np

def iacos(s, t, theta, phi):
    r, c = np.indices(s)
    tc = t / np.cos(theta)
    tr = t / np.sin(theta)
    f = np.cos(2*np.pi*(r/tr + c/tc) + phi)
    return f

