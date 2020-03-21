import math
import random
import gym
import itertools

class QLearner:
    def __init__(self, alpha=0.01, gamma=0.01, eps=0.001, sarsa=False):
        self.alpha = alpha
        self.gamma = gamma
        self.sarsa = sarsa
        self.eps = eps
        self.results = []
        self.knowledge = {}
        self.environment = gym.make('LunarLander-v2')
        self.attempt_no = 1
        self.sum = 0.0;
        for i in range(4):
            observations = itertools.product(*[[1,2,3,4] for i in range(8)])
            for j in observations:
                self.knowledge[(j,i)]=0.0
        self.upper_bounds = [
            1,1,1,1,1,1,1,1
        ]
        self.lower_bounds = [
            -1,-1,-1,-1,-1,-1,-1,-1
        ]

    def learn(self, max_attempts):
        subsum=0
        for i in range(max_attempts):
            reward_sum = self.attempt(i)
            self.sum += reward_sum
            subsum += reward_sum
            self.results.append(reward_sum)
            if(i%100==0):
                print(subsum/100.0)
                subsum=0

    def attempt(self, iteration):
        observation = self.discretise(self.environment.reset())
        done = False
        reward_sum = 0.0
        while not done:
            # if iteration%10000==999 or iteration < 20:
            #     self.environment.render()
            # for i in range(4):
            #     if (observation,i) not in self.knowledge:
            #         self.knowledge[(observation,i)]=0.0
            action = self.pick_action(observation)
            new_observation, reward, done, info = self.environment.step(action)
            new_observation = self.discretise(new_observation)
            # for i in range(4):
            #     if (new_observation,i) not in self.knowledge:
            #         self.knowledge[(new_observation,i)]=0.0
            # if done and reward_sum<499:
            #     reward=-1#-1000
            # else:
            #     reward=0#0.0
            if self.sarsa:
                self.update_knowledge_SARSA(action, observation, new_observation, reward)
            else:
                self.update_knowledge(action, observation, new_observation, reward)
            reward=1
            observation = new_observation
            reward_sum += reward
        self.attempt_no += 1
        return reward_sum

    def discretise(self, observation):
        bucket_count = 4;
        for i in range(8):
            observation[i]=max(self.lower_bounds[i]+0.000001,min(self.upper_bounds[i],observation[i]))
        res = []
        for i in range(8):
            res.append(math.ceil((observation[i]-self.lower_bounds[i])/(self.upper_bounds[i]-self.lower_bounds[i])*bucket_count))
        # x_coord_bucket = 1 if observation[0] < 0 else 2
        # x_velocity_bucket = 1 if observation[1] < 0 else 2
        # angle_coord_bucket = 1 if observation[2] < 0 else 2
        # angle_velocity_bucket = 1 if observation[3] < 0 else 2
        return tuple(res)#x_coord_bucket, x_velocity_bucket, angle_coord_bucket, angle_velocity_bucket

    def pick_action(self, observation):
        if (random.random()>1-self.eps):
            return self.environment.action_space.sample()
        res = 0;
        max_res=-100000000;
        for i in range(4):
            if max_res<self.knowledge[(observation, i)]:
                max_res = self.knowledge[(observation, i)]
                res = i
        return res
        

    def update_knowledge(self, action, observation, new_observation, reward):

        self.knowledge[(observation,action)] = (1.0 - self.alpha) * self.knowledge[(observation,action)] + self.alpha * (reward + self.gamma * 
            max(self.knowledge[(new_observation,0)], self.knowledge[(new_observation,1)]) ) 
            
        
        # else:
        #     self.knowledge[(observation,action)] = 0.99 * self.knowledge[(observation,action)] + 0.01 * reward_sum

    def update_knowledge_SARSA(self, action, observation, new_observation, reward):
        self.knowledge[(observation,action)] = self.knowledge[(observation,action)] + self.alpha * (reward + 
                    self.gamma * self.knowledge[(new_observation, self.pick_action(observation))] 
                    - self.knowledge[(observation,action)] 
                 )



if __name__ == '__main__':
    learner = QLearner()
    learner.learn(100000)
    print(learner.sum/100000)