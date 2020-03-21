import sys
from functools import reduce
def Average(lst): 
    return reduce(lambda a, b: float(a) + float(b), lst) / len(lst) 

if __name__ == '__main__':
    if(len(sys.argv)==3):
        with open(sys.argv[1],'r') as f:
            lines = f.readlines()
            split_lines = [line.split(';') for line in lines]
            avgs = [str(Average(l))+'\n' for l in split_lines]
            with open(sys.argv[2],'w+') as f2:
                f2.write(sys.argv[2].split('/')[-1]+'\n')
                f2.writelines(avgs)
    else:
        print("pass at least 3 params")