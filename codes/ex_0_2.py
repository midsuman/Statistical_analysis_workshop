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

# Open file
f = open('../problems/SN.txt', 'r')

# Read and ignore header lines
header = f.readline()
print header
# Loop over lines and count the number of useful lines
line_no = np.zeros(1,dtype=np.int)

#data = []
for line in f:
    #line = line.strip()
    #columns = line.split()
    #print columns
    #SN = {}
    #SN['z'] = float(columns[1])
    #SN['mu'] = float(columns[2])
    #SN['sigma'] = float(columns[3])
    #data.append(SN)
    line_no += 1

f.close()

print "Total number of useful lines in the file", line_no

mu_data = np.zeros(line_no,dtype=np.float32)
z_data = np.zeros(line_no,dtype=np.float32)
sigma_data = np.zeros(line_no,dtype=np.float32)

# Open file
f = open('../problems/SN.txt', 'r')

# Read and ignore header lines
header = f.readline()
print header

i=0

for line in f:
    line = line.strip()
    columns = line.split()
    #print columns
    z_data[i] = float(columns[1])
    mu_data[i] = float(columns[2])
    sigma_data[i] = float(columns[3])
    i += 1
f.close()

print len(sigma_data)

#mu_data = np.array(data.mu(), dtype=dtype)
#z_data = data[:]['z']
#sigma_data = data[:]['sigma']
#---------------------
#Plotting the analytical models and the data
#-------------------
fig = pl.figure()

host = SubplotHost(fig, 1,1,1)

host.set_xlabel('$z$',fontsize=21)
host.set_ylabel('$\mu$',fontsize=21)

fig.add_subplot(host)

p1 = host.plot(z,mu[0,:],'r-',lw=1.5,label="$\Omega_m = 0.2$")
p2 = host.plot(z,mu[1,:],'b--',lw=1.5,label="$\Omega_m = 0.3$")
p3 = host.plot(z,mu[2,:],'k-.',lw=1.5,label="$\Omega_m = 0.4$")
p4 = host.plot(z,mu[3,:],'m:',lw=1.5,label="$\Omega_m = 0.5$")
p5 = host.errorbar(z_data,mu_data,yerr=sigma_data,fmt='o',color='k',lw=1.5,label="SN data")

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

pl.savefig('../results/figs/mu_z_analytical_flat_SN_data.pdf',bbox_inches='tight')
pl.show()
