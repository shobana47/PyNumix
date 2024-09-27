import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
print("Output Is:")
print("One dimensional array:\n",a)
b=np.array([[10,20],[40,50]])
print("Two dimensional array:\n",b)
c=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("Three dimensional array:\n",c)
#from list
array_from_list=np.array([1,2,3,4,5])
print("Array from list:\n",array_from_list)
#from tuple
array_from_tuple=np.array((6,7,8,9))
print("Array from tuple:\n",array_from_tuple)

#using built functions
zero_array=np.zeros((3,4))
print("Zeronarray:\n",zero_array)
print("Shape of an ONE dimensional array",a.shape)
print("Shape of an TWO dimensional array",b.shape)
print("Shape of an THREE dimensional array",c.shape)
#dimensional
print("Dimensional of an a is:",a.ndim)
print("Dimensional of an b is:",b.ndim)
print("Dimensional of an c is:",c.ndim)
#size
print("Size of an array a is:",a.size)
print("size of an array b is:",a.size)
print("size of an array c is:",a.size)




