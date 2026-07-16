print('input')
n=int(input())
print('enter',n,'space separated integers')
l=list(map(int,input().split()))
k=int(input())
m=0
for i in range((len(l)-k)+1):
    if sum(l[i:i+k])>m:
        m=sum(l[i:i+k])
print('output')
print(m)
