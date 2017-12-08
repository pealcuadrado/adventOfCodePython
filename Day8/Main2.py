class Instruction:
    register=None
    action=None #+n -n
    condition=None #>,<,=,!=,>=,<=,==
    regCondition=None #register thats needs to meet the condition
    conditionValue=None

    def __init__(self,line):
        #parse line into atributes
        parts=line.split('if')
        if 'inc' in parts[0]:
            parts2=parts[0].split('inc')
            self.register=parts2[0]
            self.action=int(parts2[1])
        if 'dec' in parts[0]:
            parts2=parts[0].split('dec')
            self.register=parts2[0]
            self.action=-1*int(parts2[1])

        parts3=None
        for sign in ['<','>','==','!=','>=','<=']:
            if sign in parts[1]:
                self.condition=sign
                parts3=parts[1].split(sign)
        self.regCondition=parts3[0]
        self.conditionValue=int(parts3[1])

    def compare(self,valueToCompare):
        if(self.condition)=='<':
            return (valueToCompare < self.conditionValue)
        elif(self.condition)=='>':
            return (valueToCompare > self.conditionValue)
        elif (self.condition) == '==':
            return (valueToCompare == self.conditionValue)
        elif (self.condition) == '!=':
            return (valueToCompare != self.conditionValue)
        elif (self.condition) == '>=':
            return (valueToCompare >= self.conditionValue)
        elif (self.condition) == '<=':
            return (valueToCompare <= self.conditionValue)


    def printObj(self):
        print "{0} {1} {2} {3} {4}".format(self.register,self.action,self.condition,self.regCondition,self.conditionValue)

dataInput=[]
with open('data') as f:
    dataInput=f.readlines()
    dataInput=map(lambda x: x.replace(' ','').replace('\n',''),dataInput)

instructionsList=[]
for line in dataInput:
    instructionsList.append(Instruction(line))

states={}
highValue=0
for i in instructionsList:
    value=0
    valueToCompare=0
    if i.register in states:
        value=states.get(i.register)
    if i.regCondition in states:
        valueToCompare=states.get(i.regCondition)

    if i.compare(valueToCompare):
        value=value+i.action
        states.update({i.register:value})
        if value > highValue:
            highValue=value

print highValue

