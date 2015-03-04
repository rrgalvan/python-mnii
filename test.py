# -*- coding: utf-8 -*-

f = lambda x: x**3 + 4*x**2 -3*x -5

a, b = 1, 2

assert f(a)*f(b)<0,  "No se verifican hipótesis del T. Bolzano"

kmax = 6
for k in range(kmax):
    c = 0.5*(a+b)
    print "[a,b]=[%f,%f], c=%f" % (a,b,c)    
    if f(a)*f(c)<0:
        b=c
    else:
        a=c
