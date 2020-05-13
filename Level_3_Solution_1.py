def solution(l):
    t = 0
    p = [0]*len(l)

    for i in range(1, len(l)-1):
        for j in range(i):
            if(l[i]%l[j]==0):
                p[i]+=1
    for i in range(2, len(l)):
        for j in range(1, i):
            if(l[i]%l[j]==0):
                t += p[j]
    return t 
