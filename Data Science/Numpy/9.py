#Linear Regression From Scratch


import numpy as np

#Generate synthetic data:
""""
    X:200 samples, 1 feature (random)
    y = 3*X + 5 + noise
"""

np.random.seed(42) #for reproducibility

X=np.random.rand(200,1)
noise=np.random.randn(200,1)*0.5
y=3*X+5+noise

#Fit using closed-form normal equation (no sklearn).
X_design=np.hstack((np.ones((200,1)),X))

beta=np.linalg.inv(X_design.T @ X_design) @ X_design.T @ y
intercept=beta[0,0]
slope=beta[1,0]

#Print estimated slope and intercept.
print("Estimated Slope:",slope)
print("Estimated intercept:",intercept) 