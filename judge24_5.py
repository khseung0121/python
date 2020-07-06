instr = input().split()
count=0
for i in range(len(instr)):
    if instr[i].strip(',.')=='the':
        count+=1
print(count)
