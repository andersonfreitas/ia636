# -*- encoding: utf-8 -*-
# Module iacooccurrenceimport numpy as np
#import scipy.ndimage as scind
#from scipy.linalg import toeplitz

from cpmorphology import fixup_scipy_ndimage_result as fix

labels = labels.astype(int)
nlevels = quantized_image.max() + 1
nobjects = labels.max()
if scale_i < 0:
    scale_i = -scale_i
    scale_j = -scale_j
if scale_i == 0 and scale_j > 0:
    image_a = quantized_image[:, :-scale_j]
    image_b = quantized_image[:, scale_j:]
    labels_ab = labels_a = labels[:, :-scale_j]
    labels_b = labels[:, scale_j:]
elif scale_i > 0 and scale_j == 0:
    image_a = quantized_image[:-scale_i, :]
    image_b = quantized_image[scale_i:, :]
    labels_ab = labels_a = labels[:-scale_i, :]
    labels_b = labels[scale_i:, :]
elif scale_i > 0 and scale_j > 0:
    image_a = quantized_image[:-scale_i, :-scale_j]
    image_b = quantized_image[scale_i:, scale_j:]
    labels_ab = labels_a = labels[:-scale_i, :-scale_j]
    labels_b = labels[scale_i:, scale_j:]
else:
    # scale_j should be negative
    image_a = quantized_image[:-scale_i, -scale_j:]
    image_b = quantized_image[scale_i:, :scale_j]
    labels_ab = labels_a = labels[:-scale_i, -scale_j:]
    labels_b = labels[scale_i:, :scale_j]
equilabel = ((labels_a == labels_b) & (labels_a > 0))
if np.any(equilabel):

    Q = (nlevels*nlevels*(labels_ab[equilabel]-1)+
         nlevels*image_a[equilabel]+image_b[equilabel])
    R = np.bincount(Q)
    if R.size != nobjects*nlevels*nlevels:
        S = np.zeros(nobjects*nlevels*nlevels-R.size)
        R = np.hstack((R, S))
    P = R.reshape(nobjects, nlevels, nlevels)
    pixel_count = fix(scind.sum(equilabel, labels_ab,
                                np.arange(nobjects, dtype=np.int32)+1))
    pixel_count = np.tile(pixel_count[:,np.newaxis,np.newaxis],
                          (1,nlevels,nlevels))
    return (P.astype(float) / pixel_count.astype(float), nlevels)
else:
    return np.zeros((nobjects, nlevels, nlevels)), nlevels

