print('input')
n=int(input())
l=[]
print('Enter 2 space separated integers as input')
for i in range(n):
    l2=list(map(int,input().split()))
    l.append(l2)
print('output')
if n==1:
    print(l[0][0],end=' ')
    print(l[0][1])
else:
    index=1
    j=0
    while j<len(l)-1:
        if l[j][index]>=l[j+1][index-1]:
            l[j].pop()
            l[j].extend(l[j+1][1:])
            l.remove(l[j+1])
        else:
            j+=1
    for i in l:
        print(i[0],end=' ')
        print(i[1])
