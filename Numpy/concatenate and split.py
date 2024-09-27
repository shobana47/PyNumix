import numpy as np
x=np.array([1,2,3])
y=np.array([8,9,33])
join=np.concatenate([x,y])
print(join)
x1,x2=np.split(join,[2])
print(x1,x2)

