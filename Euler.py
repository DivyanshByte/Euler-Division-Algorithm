print("HCF and LCM using Euler Division Algorithm")
a = input("Enter Numbers only 2 seperated by comma: ").split(",")
a.sort()
numbers = list(map(int,a))
b = numbers.copy()
import time
start = time.time()
current = numbers[1]
while 0 not in numbers:
	numbers[1] = numbers[1]%numbers[0]
	numbers.sort()
end = time.time()
print("HCF:",numbers[1])
print("LCM:",int((b[0]*b[1])/numbers[1]))
print("Time Taken:",end-start)