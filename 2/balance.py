import math
import random
import gym


class QLearner:
    def __init__(self, alpha=0.1, gamma=0.01, eps=0.0):
        self.alpha = alpha
        self.gamma = gamma
        self.eps = eps
        self.results = []
        self.knowledge = {}
        self.environment = gym.make('CartPole-v1')
        self.attempt_no = 1
        self.sum = 0.0;
        self.upper_bounds = [
            self.environment.observation_space.high[0],
            0.5,
            self.environment.observation_space.high[2],
            math.radians(50)
        ]
        self.lower_bounds = [
            self.environment.observation_space.low[0],
            -0.5,
            self.environment.observation_space.low[2],
            -math.radians(50)
        ]

    def learn(self, max_attempts):
        for i in range(max_attempts):
            reward_sum = self.attempt(i)
            self.sum += reward_sum
            self.results.append(reward_sum)
        #    print(reward_sum)

    def attempt(self, iteration):
        observation = self.discretise(self.environment.reset())
        done = False
        reward_sum = 0.0
        while not done:
            # if iteration%1000==999 or iteration < 20:
            #    self.environment.render()
            if (observation,0) not in self.knowledge:
                self.knowledge[(observation,0)]=0.0
            if (observation,1) not in self.knowledge:
                self.knowledge[(observation,1)]=0.0
            action = self.pick_action(observation)
            new_observation, reward, done, info = self.environment.step(action)
            new_observation = self.discretise(new_observation)
            if (new_observation,0) not in self.knowledge:
                self.knowledge[(new_observation,0)]=0.0
            if (new_observation,1) not in self.knowledge:
                self.knowledge[(new_observation,1)]=0.0
            if done and reward_sum<499:
                reward=-1#-1000
            else:
                reward=0#0.0
            self.update_knowledge(action, observation, new_observation, reward)
            reward=1
            observation = new_observation
            reward_sum += reward
        self.attempt_no += 1
        return reward_sum

    def discretise(self, observation):
        bucket_count = 6;
        res = []
        for i in range(4):
            res.append(math.ceil((observation[i]-self.lower_bounds[i])/(self.upper_bounds[i]-self.lower_bounds[i])*bucket_count))
        # x_coord_bucket = 1 if observation[0] < 0 else 2
        # x_velocity_bucket = 1 if observation[1] < 0 else 2
        # angle_coord_bucket = 1 if observation[2] < 0 else 2
        # angle_velocity_bucket = 1 if observation[3] < 0 else 2
        return res[0], res[1], res[2], res[3]#x_coord_bucket, x_velocity_bucket, angle_coord_bucket, angle_velocity_bucket

    def pick_action(self, observation):
        if (random.random()>1-self.eps):
            return self.environment.action_space.sample()
        return 0 if self.knowledge[(observation,0)]>self.knowledge[(observation,1)] else 1

        

    def update_knowledge(self, action, observation, new_observation, reward):

        self.knowledge[(observation,action)] = (1.0 - self.alpha) * self.knowledge[(observation,action)] + self.alpha * (reward + self.gamma * 
            max(self.knowledge[(new_observation,0)], self.knowledge[(new_observation,1)]) ) 
            
        
        # else:
        #     self.knowledge[(observation,action)] = 0.99 * self.knowledge[(observation,action)] + 0.01 * reward_sum

    def SARSA(self, action, new_action, observation, new_observation, reward):
        self.knowledge[(observation,action)] = 
            (1.0 - self.alpha) * self.knowledge[(observation,action)] 
            + self.alpha * (reward + self.gamma * max(
                        self.knowledge[(new_observation,0)], 
                        self.knowledge[(new_observation,1)]) ) 


if __name__ == '__main__':
    learner = QLearner()
    learner.learn(10000)
    print(learner.sum/10000)