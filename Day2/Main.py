rows=[]
with open('data') as f:
    rows = f.readlines()

def getMin(row):
    min=int(row[0])
    for elem in row:
        if int(elem) < min:
            min=int(elem)
    return min

def getMax(row):
    max=int(row[0])
    for elem in row:
        if int(elem) > max:
            max=int(elem)
    return max

def getDivisibleResult(row):
    row=map(lambda x: int(x),row)
    init=0
    while init < len(row):
        for i in range(init,len(row)-1):
            if row[init] % row[i+1] == 0:
                return row[init]/row[i+1]
            if row[i+1] % row[init] == 0:
                return row[i+1]/row[init]
            i=i+1
        init=init+1


sum=0
sum2=0
for row in rows:
    elements=row.replace('\n','').split('\t')
    dif= getMax(elements) - getMin(elements)
    sum=sum+int(dif)
    print(elements)
    sum2=sum2+getDivisibleResult(elements)
    print str(sum2)

print str(sum)
print str(sum2)