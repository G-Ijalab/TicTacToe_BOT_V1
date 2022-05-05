# Winning dataset preparation 

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
 
ds=[]
f=open('gameplay.txt','r')

for i in f.read().split('\n'):  
    l,j=[],0
    while j<len(i):
        if i[j]=='(':
            t=(int(i[j+1]),int(i[j+4]))
            l.append(t)
        j+=1
    if len(l)==9:
        ds.append(l)

sds=[]
count=1
for l in ds:
     print('count : ',count)
     turn_count,dflag,i=5,True,0
     while turn_count>0:
         val1=player1.plot(l[i])
         if val1==-1:
             continue
         elif val1:
            print('Player 1 Won!!!')
            platprint()
            dflag=False
            break
         if turn_count==1:
            turn_count-=1
            continue
         val2=player2.plot(l[i+1])
         if val2==-1:
            continue
         elif val2:
            print('Player 2 Won!!!')
            platprint()
            dflag=False
            sds.append(l[:i+2])
            break
         platprint()
         turn_count-=1
         i+=2
     if turn_count==0 and dflag:
          print('Game Draw?!!!')
          platprint()
          sds.append(l)
     count+=1
     m=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
     print('*'*15)

f=open('W_gameplay.txt','w')
for i in sds:
    val=str(i)+'\n'
    f.write(val)
f.close()