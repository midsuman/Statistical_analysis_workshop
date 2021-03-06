import numpy as np
import matplotlib.pyplot as pl
from mpl_toolkits.axes_grid1.parasite_axes import SubplotHost
import const as const
import cosmo_func as cosmo


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
host.set_ylabel('Frequency',fontsize=21)

fig.add_subplot(host)
hist, edge = np.histogram(z_data,500,(0.,20.))

print hist
print edge
#pl.hist(z_data,bins=20)
p1 = host.hist(z_data,bins=50,histtype='bar')

#leg = pl.legend(loc=2,fontsize=18)

pl.draw()

pl.savefig('../results/figs/z_hist.pdf',bbox_inches='tight')
pl.show()
#Checking if git can upload the codes
