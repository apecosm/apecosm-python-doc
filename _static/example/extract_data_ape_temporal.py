import os
import sys
sys.path.insert(0, os.path.abspath('../python/'))
import apecosm
import xarray as xr

filename = '_static/example/data/'
mesh_file = '_static/example/data/mesh_mask.nc'

# definition of the domain to extract
OMZ_PERU = {'lon': [-90, -70, -70, -90, -90], 'lat': [-20, -20, 5, 5, -20]}

beng_dat = apecosm.extract_oope_data(filename, mesh_file, OMZ_PERU)
beng_dat_tmean = apecosm.extract_time_means(beng_dat, None) 
print('\n@@@@@@@@@@@@@@@@@@ Benguela time mean')
print(beng_dat_tmean)
