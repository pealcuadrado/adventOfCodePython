data=[]
with open('Data') as f:
    data=f.readlines()
data=map(lambda x: int(x.replace('\n','')),data)
limit_inf=0
limit_sup=len(data)-1

finish=False
count=0
actualPosition=0
nextPosition=0
while finish==False:
    actualPosition=nextPosition
    nextPosition=nextPosition+data[actualPosition]
    if data[actualPosition]>=3:
        data[actualPosition] = data[actualPosition] - 1
    else:
        data[actualPosition]=data[actualPosition]+1
    count+=1
    if nextPosition < limit_inf or nextPosition > limit_sup:
        finish=True
print count
