data=None
with open('data') as f:
    data= f.readlines()

data=map(lambda x: x.replace('\n',''),data)

validData=0

def transform(word):
    result=''
    abcedary='abcdefghijklmnopqrstuvwxyz'
    for l in abcedary:
        if word.count(l) > 0:
            result=result+l+str(word.count(l))
    return result

wordlist=[]
for row in data:
    wordlist=[]
    words=row.split(' ')
    for word in words:
        if transform(word) not in wordlist:
            wordlist.append(transform(word))
    if len(wordlist)==len(words):
        validData=validData+1

print validData