#dataInput=[0,2,7,0]
dataInput=[2,8,8,5,4,2,3,1,5,5,1,2,15,13,5,14]
dataHistory=[]
dataHistory.append((0,dataInput))

def getHigher(data):
    res=tuple
    res=(0,data[0])
    for i in range(1,len(data)):
        if data[i] > res[1]:
            res=(i,data[i])
    return res

def updateArray(index,value):
    data=list(dataInput)
    maxIndex=len(data)-1
    data[index]=0
    for i in range(index+1,index+value+1):
        while i > maxIndex:
            i= i-maxIndex-1
        data[i]=data[i]+1
    return data

steps=0
end=False
while end==False:
    steps=steps+1
    index,value=getHigher(dataInput)
    updatedArray=updateArray(index,value)
    if updatedArray in map(lambda (k,v): v,dataHistory):
        end=True
    else:
        dataHistory.append((steps,updatedArray))
        dataInput=updatedArray

print steps-map(lambda (k,v): v,dataHistory).index(updatedArray)