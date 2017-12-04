data=None
with open('data') as f:
    data= f.readlines()

data=map(lambda x: x.replace('\n',''),data)

validData=0

wordlist=[]
for row in data:
    wordlist=[]
    words=row.split(' ')
    for word in words:
        if word not in wordlist:
            wordlist.append(word)
    if len(wordlist)==len(words):
        validData=validData+1

print validData