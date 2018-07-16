from random import random as rnd
from math import ceil,floor
from matplotlib import pyplot as plt
tri = []
tp = []
rect = []
class line:
    def __init__(self,ids,A,B):
        ##Line AB represented as ax + by = c
        self.id = ids
        self.A = A
        self.B = B
        self.a = float(B[1] - A[1])
        self.b = float(A[0] - B[0])
        self.c = float(self.a*(A[0]) + self.b*(A[1]))    
    def show(self):
        print(' {} = {}x + {}y  = {} >>> {} | {}'.format(self.id,self.a,self.b,self.c,self.A,self.B))
    def show2(self):
        return(self.A,self.B)
class triangle:
    def __init__(self,a,b,c,id1,id2,id3):
        self.X = a
        self.Y = b
        self.Z = c
##        self.Line1 = line(int(rnd()*100),)
        self.lines = (id1,id2,id3)
    def show(self):
        print('{} >>> {},{},{}'.format(self.lines,self.X,self.Y,self.Z))
class rectangle:
    def __init__(self,a,b,c,d,id1,id2,id3,id4):
        self.P = a
        self.Q = b
        self.R = c
        self.S = d
        self.lines = (id1,id2,id3,id4)
    def show(self):
        print('{} >>> {},{},{},{}'.format(self.lines,self.P,self.Q,self.R,self.S))

def lineLineIntersection(line1,line2):
    determinant = line1.a*line2.b - line2.a*line1.b
    if (determinant == 0):
        return ()
    else:
        x = (line2.b * line1.c - line1.b * line2.c)/determinant
        y = (line1.a * line2.c - line2.a * line1.c)/determinant
        return (round(x,2), round(y,2))
def find_triangle(lineA,lineB,lineC):
    p = []
    p.append(lineLineIntersection(lineA,lineB))
    p.append(lineLineIntersection(lineB,lineC))
    p.append(lineLineIntersection(lineC,lineA))
    tmp = False
    for i in p:
        if(len(i)==0):
            tmp = True
    if(tmp==False):
        tri.append(
            triangle(p[0],p[1],p[2],lineA.id,lineB.id,lineC.id)
                   )
def find_rectangle(lineA,lineB,lineC,lineD):
    global rectangle
    p = []
    p.append(lineLineIntersection(lineA,lineB))
    p.append(lineLineIntersection(lineB,lineC))
    p.append(lineLineIntersection(lineC,lineD))
    p.append(lineLineIntersection(lineD,lineA))
    tmp = False
    for i in p:
        if(len(i)==0):
            tmp = True
    if(tmp==False):
         rect.append(rectangle(p[0],p[1],p[2],p[3],lineA.id,lineB.id,lineC.id,lineD.id)
             )
    
## line 1 >> x1 =AB.A[0] , y1 =AB.A[1] , x2 =AB.B[0] , y2 =AB.B[1]

## line 2 >> x3 =CD.A[0] , y3 =CD.A[1] , x4 =CD.B[0] , y4 =CD.B[1]

pt =[]
#this is the input 
n = 5
##x = [0,5,1,6,2,7]
##y = [0,5,0,5,0,5]
##x = [1,4,2,2,3,7,4,3]
##y = [2,7,3,5,5,5,7,4]
##x = [2,3,2,3,2,3,2,3]
##y = [2,2,3,3,4,4,5,5]
##1,2,4,7 
##2,3,2,5
##3,5,7,5
##4,7,3,4
for i in range(n):
    
    x1 = int(rnd()*100)%10
    y1 = int(rnd()*100)%10
    x2 = int(rnd()*100)%10
    y2 = int(rnd()*100)%10
##    x1 = x[i]
##    y1 = y[i]
##    x2 = x[i+1]
##    y2 = y[i+1]
##    i=2+i
    rd = int(rnd()*100)
    plt.plot((x1,x2),(y1,y2),label = str(rd))
    pt.append(line(rd,(x1,y1),(x2,y2)))
    tp.append(rd)
pt.append(pt[0])
pt.append(pt[1])
pt.append(pt[2])
other = []
##uncomment to show all the lines 
##for i in range(n):
##    pt[i].show()
if(n>=4):
    for i in range(n):
##        print('{},{},{} >>>{}'.format(pt[i].show2(),pt[i+1].show2(),pt[i+2].show2()
##                                      ,find_triangle(pt[i],pt[i+1],pt[i+2])
##                                      )
##              )
        find_triangle(pt[i],pt[i+1],pt[i+2])
        find_rectangle(pt[i],pt[i+1],pt[i+2],pt[i+3])
else:
##    print('{},{},{} >>>{}'.format(pt[0].show2(),pt[1].show2(),pt[2].show2()
##                                  ,find_triangle(pt[0],pt[1],pt[2])
##                                  )
##          )
    find_triangle(pt[0],pt[1],pt[2])

for k in tri:
    k.show()
    plt.scatter([k.X[0],k.Y[0],k.Z[0]],[k.X[1],k.Y[1],k.Z[1]])

for k in rect:
    k.show()
##    plt.scatter([k.X[0],k.Y[0],k.Z[0]],[k.X[1],k.Y[1],k.Z[1]])
print('triangle ={}, rectangle = {},special Triangle ={}'.format(len(tri),len(rect)/2,len(tri)-len(rect)/2))
plt.legend()
plt.show()
