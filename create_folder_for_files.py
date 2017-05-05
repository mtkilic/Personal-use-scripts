import shutil
import os

source = 'C:/Users/kilicm/Desktop/images/'

files = os.listdir(source)

subdir_root = 'C:/Users/kilicm/Desktop/images/'
for f in files:
    chart_type = f.split('_')[0] # splits by "_" and get the first index
    ranked_type = f.split('_')[1]

    mds_type = f.split('.png')[0].split('_')[-1]
    
    subdir_name = "".join(chart_type+"_"+ranked_type+"_"+mds_type)
    subdir = os.path.join( subdir_root, subdir_name ) # path to dir
    if not os.path.exists(subdir): # if the dir does not exist , create it
        os.makedirs(subdir)

    f_src = os.path.join( source, f) # full path to source file
    f_dest = os.path.join( subdir, f) # full path to new destination file
    shutil.move( f_src, f_dest ) 
