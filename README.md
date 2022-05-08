# Reacher-v2_Reinforcement_Learning
Rienforcement Learning Algorithm to solve the continuous control problem Reacher-v2. The algorithm implemented within this project is
the Soft Actor Critic Algorithm. The SAC algorithm is implemented using the pytorch library and openai gym library. It is simulated using
MuJoCo pysics environment. 

## Reacher-V2 Environment 
The original Reacher-V2 environment provides observations of the world in a 'ndarray' with 11 float values providing information about the world, a reward
per step, a done bool

### What Each Value Means
0 = Cosine of the angle of the first arm   
1 = cosine of the angle of the second arm
2 = sine of the angle of the first arm  
3 = sine of the angle of the second arm  
4 = x-coorddinate of the target 
5 = y-coorddinate of the target  
6 = angular velocity of the first arm    
7 = angular velocity of the second arm  
8 = x-value of position_fingertip - position_target 
9 = y-value of position_fingertip - position_target
10 = z-value of position_fingertip - position_target (0 since reacher is 2d and z is same for both)

## Wrapper Changes to Accomodate the task
The original reacher-v2 ebvironment does not provide a 'True' value for done when the fingertip reaches the target.
This is an issue as we want to reward the model for reaching the target and also reset the environment when it does.
So a wrapper functionality was added to check the values of the 8th and 9th index of the 'ndarray' which correspond to the distance
between the finger tip and the target. We check to see of both these values are between -0.01 and 0.01 to see if the model has reached 
the target. If so, the reward for the step is changed to 50 and 'done' is set to 'True' causing the episode to end and a new one to start.


## Untrained Model:
![](https://github.com/RikishK/Reacher-v2_Reinforcement_Learning/blob/master/Untrained_Model.gif) 

## 1000 Episodes of Training: 
![](https://github.com/RikishK/Reacher-v2_Reinforcement_Learning/blob/master/1000_Episode_Train.gif)

## 10,000 Episodes of Training:
![](https://github.com/RikishK/Reacher-v2_Reinforcement_Learning/blob/master/10000_episode_train.gif)
