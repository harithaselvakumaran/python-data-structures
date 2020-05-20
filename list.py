fname=open('list.txt')
lst=list()
for lines in fname:
    line=lines.rstrip()

    for word in line.split():
        if not word in lst:
            lst.append(word)
lst.sort()
print(lst)
