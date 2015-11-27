import os
import numpy as np
from get_params import get_params
from get_local_features import get_local_features

params=get_params()
ID =open(os.path.join(params['root'],params['database'],'train','ImageIDs.txt'), 'r')
desc=get_local_features(params,os.path.join(params['root'],params['database'],'train','images',str(ID.readline()).replace('\n','') + '.jpg'))
for line in ID:
    x=get_local_features(params,os.path.join(params['root'],params['database'],'train','images',str(line).replace('\n','') + '.jpg'))
    desc=np.concatenate((desc,x))
ID.close()

codebook=train_codebook(params,desc)

ID =open(os.path.join(params['root'],params['database'],'val','ImageIDs.txt'), 'r')
desc_val=get_local_features(params,os.path.join(params['root'],params['database'],'val','images',str(ID.readline()).replace('\n','') + '.jpg'))
for line in ID:
    x=get_local_features(params,os.path.join(params['root'],params['database'],'val','images',str(line).replace('\n','') + '.jpg'))
    desc_val=np.concatenate((desc,x))
ID.close()
