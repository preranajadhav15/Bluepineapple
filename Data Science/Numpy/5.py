import numpy as np

A=np.random.randint(1,100,12).reshape(3,4)
print("First Matrix:",A)

B=np.random.randint(1,100,8).reshape(4,2)
print("Second Matrix:",B)

C=A @ B
print("A @ B:",C)

print("Is (A.T).T equal to A?:",np.allclose((A.T).T,A))

I=np.identity(max(A.shape),dtype="int")
AI=A@I 
print("Is A @ I equal to A:",np.allclose(AI,A))
print("A  @ I:\n",AI)