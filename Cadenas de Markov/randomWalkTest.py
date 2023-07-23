import numpy as np

def vector(pi0, A, n):
    
    pi = pi0
    for i in range(n):
        pi = pi.dot(A)
    return pi

A = np.array([(0.2, 0.6, 0.2),
 (0.3,   0, 0.7),
  (0.5,   0, 0.5)
  ])
pi0 = np.array([0,1,0])

# [0.35191, 0.21245, 0.435164]  
pi = vector(pi0,A, 100000)
print(pi, " ", sum(pi))
