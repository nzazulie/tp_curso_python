
# coding: utf-8

# In[9]:

import numpy as np
import netCDF4
import matplotlib.pyplot as plt
import mpl_toolkits.basemap as bm
get_ipython().magic('matplotlib inline')


# In[10]:

path = '/home/usuario/wpc/wpc-original/Clase_3/'
file = 'pr_Amon_CanESM2_historical_r1i1p1_193101-200512_SA.nc'
file_in = path + file
#file_in
ncfile = netCDF4.Dataset(file_in)


# In[20]:

#ncfile      #Contiene metadata del archivo (como ncdump)
pre = ncfile.variables["pr"]
pre_data = pre[100:800,:,:]*60*60*24
#ncfile.close()
plt.plot(pre_data[:,3,10])
plt.grid()
plt.title(pre.long_name )
plt.ylabel(pre.long_name + "(mm/day)")
plt.xlabel("Time")


# In[14]:

pre.ncattrs()


# In[16]:

pre.long_name


# In[21]:

#Graficar un campo de PP
#Extraigo lat y lon


# In[ ]:



