def strlenequal(a,b): 
 l1=len(a) 
 l2=len(b) 
 if(l1!=l2): 
 return(a,"not equals to",b) 
 else: 
 c=" " 
 for i in range(l1): 
 c+=b[i]+a[i] 
 return(a,b,c) 
a=input() 
b=input() 
k=strlenequal(a,b) 
print(k)
