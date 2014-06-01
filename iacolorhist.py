# -*- encoding: utf-8 -*-
# Module iacolorhistfrom numpy import *

def iacolorhist(f, mask=None):
    from iaerror import iaerror
    from iahistogram import iahistogram

    WFRAME=5
    f = asarray(f)
    if len(f.shape) == 1: f = f[newaxis,:]
    if not f.dtype == 'uint8':
      iaerror('error, can only process uint8 images')
      return
    if not f.shape[0] == 3:
      iaerror('error, can only process 3-band images')
      return

    r,g,b = 1.*f[0,:,:], 1.*f[1,:,:], 1.*f[2,:,:]

    n_zeros = 0
    if mask:
      n_zeros = f.shape[0]*f.shape[1]-len(nonzero(ravel(mask)))
      r,g,b = mask*r, mask*g, mask*b

    hrg = zeros((256,256), int32); hbg=hrg+0; hrb=hrg+0
    img = 256*r + g; m1 = max(ravel(img))
    aux = iahistogram(img.astype(int32)); aux[0] = aux[0] - n_zeros
    put(ravel(hrg), range(m1+1), aux)
    img = 256*b + g; m2 = max(ravel(img))
    aux = iahistogram(img.astype(int32)); aux[0] = aux[0] - n_zeros
    put(ravel(hbg), range(m2+1), aux)
    img = 256*r + b; m3 = max(ravel(img))
    aux = iahistogram(img.astype(int32)); aux[0] = aux[0] - n_zeros
    put(ravel(hrb), range(m3+1), aux)
    m=max(max(ravel(hrg)),max(ravel(hbg)),max(ravel(hrb)))
    hc=m*ones((3*WFRAME+2*256,3*WFRAME+2*256))
    hc[WFRAME:WFRAME+256,WFRAME:WFRAME+256] = transpose(hrg)
    hc[WFRAME:WFRAME+256,2*WFRAME+256:2*WFRAME+512] = transpose(hbg)
    hc[2*WFRAME+256:2*WFRAME+512,WFRAME:WFRAME+256] = transpose(hrb)
    return hc

