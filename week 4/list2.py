fh=open("list2.txt")
count=0
for line in fh:
    if not line.startswith('From '):continue
    lines=line.split()
    word=lines[1]
    print(word)
    count=count+1
print('There were',count,'lines in the file with From as the first word')
