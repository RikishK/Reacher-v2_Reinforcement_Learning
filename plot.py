import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

rewards_reacher = np.loadtxt("mean_rewards_Reacher-v2_54.txt")
rewards_reacher = np.array(rewards_reacher)
rewards_reacher = rewards_reacher.reshape(-1)
print(rewards_reacher.shape)

wins_reacher = np.loadtxt("win_rewards_Reacher-v2_54.txt")
wins_reacher = np.array(wins_reacher)
wins_reacher = wins_reacher.reshape(-1)
print(wins_reacher.shape)

steps = np.linspace(1,9600,9600)

plt.figure(figsize=(6.5,4))
#plt.subplot(2,2,1)
plt.plot(steps, rewards_reacher, label='1', linewidth=0.7)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0), useMathText=True)
plt.grid()
plt.legend(fontsize='large')
plt.xlabel(r'Episode')
plt.ylabel(r'Average reward')
plt.tight_layout()
plt.savefig('rewards_9600.jpg', dpi=300)
plt.show()
#plt.close()

plt.figure(figsize=(6.5,4))
#plt.subplot(2,2,1)
plt.plot(steps, wins_reacher, label='2', linewidth=0.7)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0), useMathText=True)
plt.grid()
plt.legend(fontsize='large')
plt.xlabel(r'Episode')
plt.ylabel(r'Win')
plt.tight_layout()
plt.savefig('wins_9600.jpg', dpi=300)
plt.show()
#plt.close()







