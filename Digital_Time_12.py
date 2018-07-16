num = [0,0,1,1,3,5,6,7,7]
times = []
def find(n,key):
    for i in range(len(n)):
        if(n[i]==key):
            return i
    return -1
def gernerate(n):
    i = n
    global num,times
    while(i>0):
        if(find(num,i)>=0):
            times.append(i)
            num.remove(i)
            break
        i = i - 1

gernerate(1)
gernerate(1)
gernerate(5)
gernerate(9)
gernerate(5)
gernerate(9)

if(len(times) == 6):
    print('{}{}:{}{}:{}{}'.format(times[0],times[1],times[2],times[3],times[4],times[5]))
else:
    print('Not possible')
