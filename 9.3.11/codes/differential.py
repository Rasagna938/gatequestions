import ctypes
import matplotlib.pyplot as plt

lib=ctypes.CDLL('./differential.so')  #loading the .so shared lib which was created from c code

lib.Xco.restype=ctypes.POINTER(ctypes.c_double) #Xco returns a pointer to an array
lib.Yco.restype=ctypes.POINTER(ctypes.c_double) #Yco returns a pointer to an array

#calling C functions to get x and y coordinates
result1=lib.Xco()
result2=lib.Yco()

x_coords=list([])
y_coords=list([])

#looping through points and store them in a list

for i in range(10000):
    x_coords.append(result1[i])
    y_coords.append(result2[i])
#plotting the points
plt.scatter(x_coords,y_coords)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('DIFFERENTIAL EQUATIONS')
plt.grid(True)
plt.show()


