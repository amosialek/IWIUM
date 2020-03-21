from balance import *
import sys
def main():
    iters = 10000
    age={}
    sets=[[0.01,0.01,0],[0.01,0.1,0],[0.01,0.1,0.1],[0.01,0.05,0.05]]
    current_age_set = sets[int(sys.argv[1])]
    alpha = current_age_set[0]
    gamma = current_age_set[1]
    eps = current_age_set[2]
    learners = []
    for i in range(10):
        learner = QLearner(alpha, gamma, eps)
        learners.append(learner)
        
        learner.learn(iters)
        print(learner.sum/iters)
    lines=[]
    for i in range(iters):
        lines.append(';'.join([str(l.results[i]) for l in learners])+'\n')
    with open("res2/res_"+str(alpha)+'_'+str(gamma)+'_'+str(eps)+'.csv','w+') as f:
        f.writelines(lines)

if __name__ == '__main__':
    #if(len(sys.argv)==3):
    main()
    #else:
    #    print("pass at least 3 params")
