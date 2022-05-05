import pickle
import numpy as np
from system import System
n_test = 6
system_type = 'Reacher-v2'
system = System(system=system_type, reward_scale=100)
tr_epsds = 200
epsd_steps = 1000
mean_rewards = []
win_rewards = []
for i in range(1,6):
    print("NEW TRAIN: ", i)
    if i == 1:
        m, r = system.train_agent(tr_epsds, epsd_steps)
        mean_rewards.append(m)
        win_rewards.append(r)

    else:
        m, r = system.train_agent(tr_epsds, epsd_steps, initialization=False)
        mean_rewards.append(m)
        win_rewards.append(r)
    pickle.dump(system,open(system_type+'_'+str(n_test)+'_'+str((i+5)//5)+'.p','wb'))
    np.savetxt('mean_rewards_'+system_type+'_'+str(i)+'.txt',mean_rewards)
    np.savetxt('win_rewards_'+system_type+'_'+str(i)+'.txt',win_rewards)


