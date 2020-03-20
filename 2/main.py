from balance import *
import sys
def main():
    iters = 10000
    age={}
    for alpha in range(1,11,1):
        for gamma in range(int(sys.argv[1]),int(sys.argv[2]),1):
            for eps in range(1,21,2):
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