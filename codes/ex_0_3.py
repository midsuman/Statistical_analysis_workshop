import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits.axes_grid1.parasite_axes import SubplotHost
import const as const
import cosmo_func as cosmo

h=0.7
z_ana = np.arange(0.001,2.,0.01)

z=np.arange(0.05,2.,0.1)
Omega_m = 0.3

shape_z_ana = np.asarray(z_ana.shape, dtype=np.int)
shape_z = np.asarray(z.shape, dtype=np.int)


mu_ana = np.zeros(shape_z_ana, dtype = np.float32, order = 'C')
mu = np.zeros(shape_z, dtype = np.float32, order = 'C')

#Genrating Gaussian random error with SD 0.1 magnitude and 0 mean
error = np.random.normal(0.,0.1,shape_z)

#Generating noisy data
for j in range (shape_z):
    mu[j] = cosmo.dist_modulus(z[j],Omega_m,(1.-Omega_m),h) + error[j]

#generating the fitting function
for j in range (shape_z_ana):
    mu_ana[j] = cosmo.dist_modulus(z_ana[j],Omega_m,(1.-Omega_m),h)
    
#---------------------
#Plotting the analytical models and the data
#-------------------
fig = pl.figure()

host = SubplotHost(fig, 1,1,1)

host.set_xlabel('$z$',fontsize=21)
host.set_ylabel('$\mu$',fontsize=21)

fig.add_subplot(host)

p1 = host.plot(z_ana,mu_ana,'r-',lw=1.5,label="$\Omega_m = 0.3$")

p2 = host.errorbar(z,mu,yerr=0.1,fmt='o',color='k',lw=1.5,label="SN data")

leg = pl.legend(loc=4,fontsize=18)
#host.set_ylim(0,48)

#pl.xticks(visible=False)
#pl.yticks(visible=False)
#host.yaxis.get_label().set_color(p1.get_color())
#leg.texts[0].set_color(p1.get_color())
#host.yaxis.get_label().set_color(p2.get_color())
#leg.texts[1].set_color(p2.get_color())
#host.yaxis.get_label().set_color(p3.get_color())
#leg.texts[2].set_color(p3.get_color())
#host.yaxis.get_label().set_color(p4.get_color())
#leg.texts[3].set_color(p4.get_color())
pl.draw()

pl.savefig('../results/figs/mu_z_with_random_noise.pdf',bbox_inches='tight')
pl.show()
