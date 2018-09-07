n=int(input("Enter n: "))

def foo(n):
   a=[x for x in range(2,n+1)]
   for i in a:
       if(i!=''):
           for j in a:
               if(j!=''):
                   if(i!=j and j%i==0):
                       a[a.index(j)]=''
       if(i!=''):
           yield i

for i in foo(n):
    print(i)