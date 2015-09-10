import numpy as np
import const as const

#------------------------------------------------------------------
def dist_modulus(z, Omega_m, Omega_l, h=0.7):
    #Calculates the distance modulus for a given redshift (z) and 
    #Cosmological parameters Omega_m, Omega_l and h
    
    val = D_L_flat(z, Omega_m)
    mu = 25. - 5.*(np.log10(h)) + 5.*(np.log10(val))
    return mu

#------------------------------------------------------------------
def D_L_flat(z, Omega_m):
    #Luminosity distance for flat universe Omega_tot =1
    #Fitting function from U.-L. Pen, ApJS,120:4950, 1999

    d_l = (const.c/const.H0)*(1+z)*(eta(1, Omega_m) - eta(1./(1+z), Omega_m))
   
    return d_l
#------------------------------------------------------------------

def eta(a, Omega_m):
    # eta function from U.-L. Pen, ApJS,120:4950, 1999

    s = (1 - Omega_m)/Omega_m
    val = 1./np.power(a,4.) - 0.1540*s/np.power(a,3.) + 0.4304*np.power(s,2.)/np.power(a,2.) + 0.19097*np.power(s,3.)/a + 0.066941*np.power(s,4.)
    val = np.power(val, 1./8.)
   
    eta_val = 2.*np.sqrt(np.power(s,3.)+ 1.)/val

    return eta_val

#------------------------------------------------------------------
