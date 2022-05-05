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
a=0
while a<8:
    p1=tuple(map(int,input('>>').split(' ')))
    ds1=[i for i in ds1 if i[a]==p1]
    la=[j[a+1] for j in ds1]
    p2=statistics.mode(la)
    print(p2)
    ds1=[k for k in ds1 if k[a+1]==p2]
    a+=2

print(ds1)