import sys 
def walking_avg(values):
    res=[]
    sum=0
    for i in range(10):
        sum += float(values[i])
    for i in range(9990):
        res.append(sum/10.0)
        sum-=float(values[i])
        sum+=float(values[i+10])
    return [str(r) for r in res]
    
if __name__ == '__main__':
    if(len(sys.argv)==3):
        with open(sys.argv[1],'r') as f:
            lines = f.readlines()
            split_lines = [line.split(';') for line in lines]
            transposed = list(map(list,zip(*split_lines)))
            avgs = [walking_avg(l) for l in transposed]
            transposed_avgs = list(map(list,zip(*avgs)))
            with open(sys.argv[2],'w+') as f2:
                lines=[]
                for i in range(9990):
                    lines.append(';'.join(transposed_avgs[i])+'\n')
                f2.writelines(lines)
    else:
        print("pass at least 3 params")
