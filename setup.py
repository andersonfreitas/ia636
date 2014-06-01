#!/usr/bin/env python

from distutils.core import setup, Extension

support_ext_files = ['numpy.i', 'simple_arrays.i', 'simple_arrays.cpp']
setup(name='ia636',
    version='1.3.0',
    description='',
    author='RCM',
    author_email='',
    url='',
    py_modules=[
    
        'MainPage', 'src/_MainPage',
    
        'iaapplylut', 'src/_iaapplylut',
    
        'iabwlp', 'src/_iabwlp',
    
        'iacircle', 'src/_iacircle',
    
        'iacolorhist', 'src/_iacolorhist',
    
        'iacolormap', 'src/_iacolormap',
    
        'iacomb', 'src/_iacomb',
    
        'iacontour', 'src/_iacontour',
    
        'iaconv', 'src/_iaconv',
    
        'iacooccurrence', 'src/_iacooccurrence',
    
        'iacorr', 'src/_iacorr',
    
        'iacos', 'src/_iacos',
    
        'iacrop', 'src/_iacrop',
    
        'iadct', 'src/_iadct',
    
        'iadctmatrix', 'src/_iadctmatrix',
    
        'iadft', 'src/_iadft',
    
        'iadftmatrix', 'src/_iadftmatrix',
    
        'iadftview', 'src/_iadftview',
    
        'iadither', 'src/_iadither',
    
        'iaffine', 'src/_iaffine',
    
        'iaffine3', 'src/_iaffine3',
    
        'iafftshift', 'src/_iafftshift',
    
        'iafig2img', 'src/_iafig2img',
    
        'iafloyd', 'src/_iafloyd',
    
        'iaftemplate', 'src/_iaftemplate',
    
        'iagaussian', 'src/_iagaussian',
    
        'iageorigid', 'src/_iageorigid',
    
        'iagshow', 'src/_iagshow',
    
        'iah2percentile', 'src/_iah2percentile',
    
        'iah2stats', 'src/_iah2stats',
    
        'iahaarmatrix', 'src/_iahaarmatrix',
    
        'iahadamard', 'src/_iahadamard',
    
        'iahadamardmatrix', 'src/_iahadamardmatrix',
    
        'iahistogram', 'src/_iahistogram',
    
        'iahwt', 'src/_iahwt',
    
        'iaidct', 'src/_iaidct',
    
        'iaifftshift', 'src/_iaifftshift',
    
        'iaihadamard', 'src/_iaihadamard',
    
        'iaihwt', 'src/_iaihwt',
    
        'iaimginfo', 'src/_iaimginfo',
    
        'iaind2sub', 'src/_iaind2sub',
    
        'iainterpolclosest', 'src/_iainterpolclosest',
    
        'iainterpollin', 'src/_iainterpollin',
    
        'iaisdftsym', 'src/_iaisdftsym',
    
        'iaisolines', 'src/_iaisolines',
    
        'ialabel', 'src/_ialabel',
    
        'ialblshow', 'src/_ialblshow',
    
        'ialog', 'src/_ialog',
    
        'ialogfilter', 'src/_ialogfilter',
    
        'iameshgrid', 'src/_iameshgrid',
    
        'iamosaic', 'src/_iamosaic',
    
        'ianeg', 'src/_ianeg',
    
        'ianormalize', 'src/_ianormalize',
    
        'ianshow', 'src/_ianshow',
    
        'iaotsu', 'src/_iaotsu',
    
        'iapad', 'src/_iapad',
    
        'iapca', 'src/_iapca',
    
        'iapconv', 'src/_iapconv',
    
        'iapconv2', 'src/_iapconv2',
    
        'iapercentile', 'src/_iapercentile',
    
        'iaphasecorr', 'src/_iaphasecorr',
    
        'iaplot', 'src/_iaplot',
    
        'iapolar', 'src/_iapolar',
    
        'iaptrans', 'src/_iaptrans',
    
        'iaramp', 'src/_iaramp',
    
        'iareadurl', 'src/_iareadurl',
    
        'iarec', 'src/_iarec',
    
        'iarectangle', 'src/_iarectangle',
    
        'iargb2gray', 'src/_iargb2gray',
    
        'iaroi', 'src/_iaroi',
    
        'iarot90', 'src/_iarot90',
    
        'iashow', 'src/_iashow',
    
        'iasobel', 'src/_iasobel',
    
        'iastat', 'src/_iastat',
    
        'iasub2ind', 'src/_iasub2ind',
    
        'iatcrgb2ind', 'src/_iatcrgb2ind',
    
        'iatile', 'src/_iatile',
    
        'iatiling', 'src/_iatiling',
    
        'iavarfilter', 'src/_iavarfilter',
    
        'iawcorr', 'src/_iawcorr',
    
    ],
    ext_modules=[
    
    ],
)
