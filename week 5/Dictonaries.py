#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they
#appear in the file. After the dictionary isproduced, the program reads through the dictionary using a maximum
#loop to find the most prolific committer.

fh=input('Enter file name')
fname=open(fh)
count=0
d=dict()
for lines in fname:
    if not lines.startswith('From '): continue
    line=lines.split()
    sender=line[1]
    for word in sender.split():         #If split not used then word will iterate over each letter of sender
        if word in d:                   #sender.split() gives a list with single mail id
            d[word]=d[word]+1
            #print(word,d[word])
            #print('Exists')
        else:
            d[word]=1
            #print(word,d[word])
            #print('New')
#print(d)

largest=-1                          #As we know here counters are positive
for key,count in d.items():
    if count>largest:
        largest=count
        word=key
print(word,largest)
