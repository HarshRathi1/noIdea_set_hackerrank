n,m=map(int,input().split())
arr=list(map(int,input().split()))
A=set(map(int,input().split()))
B=set(map(int,input().split()))
k=0
for i in A:
    if i in arr:
        k+=1
for j in B:
    if j in arr:
        k-=1
print(k)