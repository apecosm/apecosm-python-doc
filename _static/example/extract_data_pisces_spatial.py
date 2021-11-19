import os
import sys
sys.path.insert(0, os.path.abspath('../python/'))
import apecosm

filename = '_static/example/data/data_pisces.nc'
mesh_file = '_static/example/data/mesh_mask.nc'

beng_phy2_dat = apecosm.extract_ltl_data(filename, 'PHY2', mesh_file, 'BENGUELA', depth_max=None)

print(beng_phy2_dat)
