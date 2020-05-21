name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d=dict()
for line in handle:
    if not line.startswith('From '):continue
    line=line.split()
    word=line[5]
    main=word.split(':')
    main=main[0]
    if main in d:
        d[main]=d[main]+1
    else:
        d[main]=1

for (k,v) in sorted(d.items()):
    print(k,v)
