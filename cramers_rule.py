import numpy as np
eqn=int(input("enter number of equations"))
col=[]
for i in range(eqn):
    row=[]
    for j in range(eqn):
        z="enter"+str(j+1)+"element of"+"equation"+str(i+1)
        y=int(input(z))
        row.append(y)
    col.append(row)
a=np.array(col)
print(a)

sol=[]
for i in range(eqn):
    n="enter"+str(j+1)+" "+"value of rhs"
    x=int(input(n))
    sol.append(x)
b=np.array(sol)
print(b)

def cramer(p,q):
    co_matrix=round(np.linalg.det(p))
    det_matrix=[]
    c=p.copy()
    for i in range(eqn):
        c[:,i]=q
        print(c)
        x=np.linalg.det(c)
        det_matrix.append(x)
        c=p.copy()
        X=det_matrix/co_matrix
        print(X)

cramer(a,b)

    
    
    
    

    
    
