# -*- encoding: utf-8 -*-
# Module ianormalizefrom numpy import *

def ianormalize(f, range=[0,255]):
    from iaerror import iaerror

    f = asarray(f)
    range = asarray(range)
    if f.dtype.char in ['D', 'F']:
        iaerror('error: cannot normalize complex data')
        return None
    faux = ravel(f).astype(float)
    minimum = min(faux)
    maximum = max(faux)
    lower = range[0]
    upper = range[1]
    if upper == lower:
        iaerror('error: image is constant, cannot normalize')
        return f
    if minimum == maximum:
        g = ones(f.shape)*(upper + lower) / 2.
    else:
        g = (faux-minimum)*(upper-lower) / (maximum-minimum) + lower
    g = reshape(g, f.shape)

    T = f.dtype.char
    if T == 'b': # uint8
        if upper > 255:
            iaerror('ianormalize: warning, upper valuer larger than 255. Cannot fit in uint8 image')
        g = g.astype('b')
    g = g.astype(f.dtype) # set data type of result the same as the input image
    return g

