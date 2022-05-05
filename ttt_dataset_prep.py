#complete gameplay dataset preparation

l=[1,2,3,4,5,6]
fl=[]

for i in l:
    l1a=[i]
    l1b=[]
    for m in l:
        if m!=i:
            l1b.append(m)
    for j in l1b:
        l1a.append(j)
        l1c=[]
        for n in l1b:
            if n!=j:
                l1c.append(n)
        for k in l1c:
            l1a.append(k)
            l1d=[]
            for r in l1c:
                if r!=k:
                    l1d.append(r)
            for b in l1d:
                l1a.append(b)
                l1e=[]
                for p in l1d:
                    if p!=b:
                        l1e.append(p)
                for q in l1e:
                    l1a.append(q)
                    l1f=[]
                    for w in l1e:
                        if w!=q:
                            l1f.append(w)
                    for g in l1f:
                        l1a.append(g)
                        fl.append(l1a)
                        l1a=[i,j,k,b]
                l1a=[i,j,k]
            l1a=[i,j]
        l1a=[i]


def func1(x,y):
    lf=[]
    ls=[([],y),(y,[])]
    for i in range(1,len(y)):
        ls.append((y[0:i],y[i::]))
    for la,lc in ls:
        lb=[x,]
        li=la+lb+lc
        lf.append(li)
    return lf

fl1=[]
dds={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}

for i in fl:
    for j in func1(7,i):
        for k in func1(8,j):
            li=[[dds[x] for x in y] for y in func1(9,k)]
            fl1+=li

f=open('gameplay.txt','w')
for i in fl1:
    print(i)
    v=str(i)+'\n'
    f.write(v)
f.close()

#fl1 is the required dataset 

# Winning dataset preparation 
# Segregating dataset for first move
# and so on for each X's moves 
# Manipulate like magic
