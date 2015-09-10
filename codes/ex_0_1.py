import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits.axes_grid1.parasite_axes import SubplotHost
import const as const
import cosmo_func as cosmo

h=0.7
z=np.arange(0.001,2.,0.01)
Omega_m = np.array([0.2,0.3,0.4,0.5])

shape_Omega = np.asarray(Omega_m.shape, dtype=np.int)
shape_z = np.asarray(z.shape, dtype=np.int)

mu = np.zeros((shape_Omega, shape_z), dtype = np.float32, order = 'C')

for i in range (shape_Omega):
    for j in range (shape_z):
        mu[i,j] = cosmo.dist_modulus(z[j],Omega_m[i],(1.-Omega_m[i]),h)



fig = pl.figure()

host = SubplotHost(fig, 1,1,1)

host.set_xlabel('$z$', fontsize=20)
host.set_ylabel('$\mu$',fontsize=20)

fig.add_subplot(host)

p1 = host.plot(z,mu[0,:],'r-',lw=1.5,label="$\Omega_m = 0.2$")
p2 = host.plot(z,mu[1,:],'b--',lw=1.5,label="$\Omega_m = 0.3$")
p3 = host.plot(z,mu[2,:],'k-.',lw=1.5,label="$\Omega_m = 0.4$")
p4 = host.plot(z,mu[3,:],'m:',lw=1.5,label="$\Omega_m = 0.5$")

leg = pl.legend(loc=4,fontsize=18)
host.set_ylim(0,48)

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
pl.savefig('mu_z_analytical_flat.pdf',bbox_inches='tight')
pl.show()
