# -*- encoding: utf-8 -*-
# Module ianshowimport ia870 as ia
import ia636 as ia6
import numpy as np

def t(s):
   a = ia.iatext(s)
   b = np.pad(a,((6+4,6+4),(0+4,0+4)),'constant', constant_values=((False,False),(False,False)))
   c = np.pad(b,((1,1),(1,1)),'constant', constant_values=((True,True),(True,True)))
   return c

def timg(f):

  tFalse = t('   ')
  dy, dx = tFalse.shape
  tTrue = np.zeros_like(tFalse)
  z = np.empty(tuple(np.array(f.shape) * np.array([dy,dx]))).astype(bool)
  if f.dtype == 'bool':
    for x in np.arange(f.shape[-1]):
      for y in np.arange(f.shape[-2]):
        if f[y,x]:
          z[y*dy:y*dy+dy,x*dx:x*dx+dx] = tFalse
        else:
          z[y*dy:y*dy+dy,x*dx:x*dx+dx] = tTrue
    z=ia.ianeg(np.pad(z,((1,1),(1,1)),'constant'))
  else:
    for x in np.arange(f.shape[-1]):
      for y in np.arange(f.shape[-2]):
        z[y*dy:y*dy+dy,x*dx:x*dx+dx] = t('%3d' % f[y,x])
    z=np.pad(ia.ianeg(z),((1,1),(1,1)),'constant')
  return z

def ianshow(X, X1=None, X2=None, X3=None, X4=None, X5=None, X6=None):
  x = timg(X)
  x1,x2,x3,x4,x5,x6 = None,None,None,None,None,None
  if X1 is not None:
    x1 = ia.iadil(ia.ianeg(timg(X1)))
  if X2 is not None:
    x2 = ia.iadil(ia.ianeg(timg(X2)))
  if X3 is not None:
    x3 = ia.iadil(ia.ianeg(timg(X3)))
  if X4 is not None:
    x4 = ia.iadil(ia.ianeg(timg(X4)))
  if X5 is not None:
    x5 = ia.iadil(ia.ianeg(timg(X5)))
  if X6 is not None:
    x6 = ia.iadil(ia.ianeg(timg(X6)))
  return ia.iagshow(x,x1,x2,x3,x4,x5,x6)

