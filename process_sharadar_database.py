import pandas as pd
import os
import sys

def split_code(code):
    ls_fields = code.split('_')
    if len(ls_fields) > 2:
        dimension = ls_fields[2]
    else:
        dimension = ''
    ticker = ls_fields[0]
    indicator = ls_fields[1]
    return pd.Series({'ticker':ticker,'indicator':indicator,'dimension':dimension})
    
rootdir = os.path.dirname(os.path.realpath(sys.argv[0]))

dataset_path = os.path.join(rootdir,'config','SF1_20150301.csv')
out_path = os.path.join(rootdir,'config','SF1_post.hdf')
df_orig = pd.read_csv(dataset_path,header=None,names=['code','date','value'])
df_processed = df_orig.code.apply(split_code) #This dataframe will have 3 columns
df_processed = pd.concat([df_processed,df_orig.date,df_orig.value],axis=1)
del df_orig # Clear a bit of memory before attempting to dump to file
df_processed.to_hdf(out_path,'fund')


