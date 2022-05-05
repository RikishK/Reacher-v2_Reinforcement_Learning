import pickle
import numpy as np
from system import System
import pandas as pd

#read system from file
system = pd.read_pickle(r'model_saves/Reacher-v2_6_11.p')
print("System ready")
epsd_count = 25

system.replay_agent(epsd_count)


