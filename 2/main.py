from balance import *
import sys
def main():
    iters = 10000
    age={}
    sets=[[0.1,0,0],[0.1,0.1,0],[0.1,0.1,0.1],[0.1,0.05,0.05]]
    for age_set in sets
        alpha = age_set[0]
        gamma = age_set[1]
        eps = age_set[2]
        learners = []
        for i in range(10):
            learner = QLearner(alpha/100.0, gamma/10.0, eps/100.0)
            learners.append(learner)
            
            learner.learn(iters)
            print(learner.sum/iters)
        lines=[]
        for i in range(iters):
            lines.append(';'.join([str(l.results[i]) for l in learners])+'\n')
        with open("res/res_"+str(alpha)+'_'+str(gamma)+'_'+str(eps)+'.csv','w+') as f:
            f.writelines(lines)
    x=1

if __name__ == '__main__':
    if(len(sys.argv)==3):
        main()
    else:
        print("pass at least 3 params")