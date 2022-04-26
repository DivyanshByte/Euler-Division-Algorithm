print("HCF using Normal Factor Algorithm")
a = input("Enter Numbers only 2 seperated by comma: ").split(",")
a.sort()
numbers = list(map(int,a))
import time
def calculate_hcf(x, y):  
    # selecting the smaller number  
    if x > y:  
        smaller = y  
    else:  
        smaller = x  
    for i in range(1,smaller + 1):  
        if((x % i == 0) and (y % i == 0)):  
            hcf = i  
    return hcf

start = time.time()
hcf = calculate_hcf(numbers[0],numbers[1])
end = time.time()
print("HCF:",hcf)
print("LCM:",int((numbers[0]*numbers[1])/hcf))
print("Time Taken:",end-start)