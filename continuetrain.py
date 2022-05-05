import pickle
import numpy as np
from system import System
import pandas as pd
n_test = 6
system_type = 'Reacher-v2'
system = pd.read_pickle(r'Reacher-v2_6_2.p')
tr_epsds = 200
epsd_steps = 1000
mean_rewards = []
win_rewards = []
cont_start = 7
cont_end = 55
for i in range(cont_start,cont_end):
    print("NEW TRAIN: ", i)
    m, r = system.train_agent(tr_epsds, epsd_steps, initialization=False)
    mean_rewards.append(m)
    win_rewards.append(r)
    pickle.dump(system,open(system_type+'_'+str(n_test)+'_'+str((i+5)//5)+'.p','wb'))
    np.savetxt('mean_rewards_'+system_type+'_'+str(i)+'.txt',mean_rewards)
    np.savetxt('win_rewards_' + system_type + '_' + str(i) + '.txt', win_rewards)