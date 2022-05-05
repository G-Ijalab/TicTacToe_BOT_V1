import statistics

f=open('W_gameplay.txt','r')
ds=[]

for i in f.read().split('\n'):  
    l,j=[],0
    while j<len(i):
        if i[j]=='(':
            t=(int(i[j+1]),int(i[j+4]))
            l.append(t)
        j+=1
    if len(l)!=0:
        ds.append(l)

ds1=ds

m=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

class player:
    global m
    def __init__(self,val):
        self.nature=val
    def plot(self,coor):
        if m[coor[0]][coor[1]]==-1:
            m[coor[0]][coor[1]]=self.nature
            l=[]
            l.append(m[coor[0]])
            l.append([m[i][coor[1]] for i in range(3)])
            if coor in [(0,0),(2,2)]:
                l.append([m[i][j] for i,j in [(0,0),(1,1),(2,2)]])
            elif coor in [(2,0),(0,2)]:
                l.append([m[i][j] for i,j in [(2,0),(0,2),(1,1)]])
            flagarr=[]
            for i in l:
                flag=True
                for j in i:
                    if j!=self.nature:
                        flag=False
                flagarr.append(flag)
            if True in flagarr:
                 return 1
            else:
                 return 0    
        else:
            return -1   
            
player1=player('x')
player2=player('o')

print(' Your symbol     : X ')
print(' Computer symbol : O')
print(' Guide : ')
for i in range(1,8,3):
    strv=''
    for j in range(i,i+3):
        strv+='| {} |'.format(j)
    print(' --- '*3)
    print(strv)
print(' --- '*3)

def platprint():
    for i in m:
        str1=''
        for j in i:
            val=j
            if j==-1:
                val=' '     
            str1+='| {} |'.format(val)
        print(' --- '*3)
        print(str1)
    print(' --- '*3)

turn_count,dflag,i=5,True,0
id={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}

while turn_count>0:
    p1i=int(input('>> Enter the position : '))
    p1=id[p1i]
    val1=player1.plot(p1)
    if val1==-1:
        continue
    elif val1:
        print('You Won!!!')
        platprint()
        dflag=False
        break
    if turn_count==1:
        turn_count-=1
        continue
    ds1=[z for z in ds1 if z[i]==p1] #wseg implementation dynamic
    la=[j[i+1] for j in ds1]
    p2=statistics.mode(la)
    val2=player2.plot(p2)
    ds1=[k for k in ds1 if k[i+1]==p2]
    if val2==-1:
         continue
    elif val2:
        print('Computer Won!!!')
        platprint()
        dflag=False
        break
    platprint()
    turn_count-=1
    i+=2
if turn_count==0 and dflag:
    print('Game Draw?!!!')
    platprint()
         
print('*'*15)