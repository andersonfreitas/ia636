# -*- encoding: utf-8 -*-
# Module iagshow
from numpy import *
import ia870

def iagshow(X, X1=None, X2=None, X3=None, X4=None, X5=None, X6=None):
    g = ia870.iagshow(X,X1,X2,X3,X4,X5,X6)
    return g

