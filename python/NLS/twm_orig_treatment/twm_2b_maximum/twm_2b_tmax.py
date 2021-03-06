###Calculates three-wave-mixing effects at the 2*beta frequency for beta=10.

import math as mth
eta0=1.0;etab=1.0;etanb=1.0
alphab=0.0;alphanb=0.0;alpha0=0.0
tslot=20;nbmax=101;
nmaxt=nbmax-1;tmax=5.0;tmin=-5.0
nmaxz=10**4;zmin=-5.0
beta=10
yb=-1.0*tslot;ynb=1.0*tslot;y0=0.0
phi=[0.0 for k in range(nbmax)]
s1=0.0; s2=0.0

f= open('twmXT.txt','w+')

#Begin loop over zf values
for i in range(51):
    zf=0.1*i
    dz=(zf-zmin)/nmaxz
    dt=(tmax-tmin)/nmaxt
#   Begin loop over t
    t=tmin
    for k in range(nbmax):
        z=zmin+0.5*dz
        s1=0.0
        s2=0.0
        x0=eta0*t
        for j in range(nmaxz):
            xb=etab*(t-yb-2*beta*z)
            xnb=etanb*(t-ynb+2*beta*z)
            chi0=alpha0+(eta0**2)*z
            chib=alphab+beta*(t-yb)+z*((etab**2)-beta**2)
            chinb=alphanb-beta*(t-ynb)+z*(etanb**2-beta**2)
            s1+=mth.sin(2*chib-chi0)/(mth.cosh(xb))**2
            s2+=mth.cos(2*chib-chi0)/(mth.cosh(xb))**2
            z+=dz
        phi[k]=2.0*(etab**2)*eta0*mth.sqrt(s1**2+s2**2)*dz/mth.cosh(x0)
        t+=dt

##Attempts to capture T_max by iterating over t and looking for the value
##that corresponds to phi_max. 
for i in range(51):
    T=tmin
    Z=0.1*i
    dz=(zf-zmin)/nmaxz
    dt=(tmax-tmin)/nmaxt
    for j in range(nbmax):
        if phi[j]==max(phi):
            if T>-2.0 and T<+2.0:
                f.write(str(T)+" "+str(Z)+' \n')
        T+=dt
    Z+=dz
    
f.close()
print 'tmax done!'
