def c(A,B,C):return(C[1]-A[1])*(B[0]-A[0])>=(B[1]-A[1])*(C[0]-A[0])
def i(A,B,C,D):return c(A,C,D)!=c(B,C,D)and c(A,B,C)!=c(A,B,D)
U=int;I=input
def t():
 p,a,b=U(I()),[(*map(int,_.split(',')),)for _ in I().split()],[(*map(int,_.split(',')),)for _ in I().split()]
 for q in range(p):
  m,n,E,F=0,0,(a[q][0]+1400,a[q][1]),(b[q][0]+1400,b[q][1])
  for r in range(p):
   if i(a[q],a[(q+1)%p],b[r],b[(r+1)%p]):return"true"
   if(i(a[q],E,b[r],b[(r+1)%p])):m+=1
   if(i(b[q],F,a[r],a[(r+1)%p])):n+=1
  if m%2==1 or n%2==1:return"true"
 return"false"
for _ in' '*U(I()):print(t())
