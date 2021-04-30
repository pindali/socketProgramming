import numpy as np
import time
def binary_search(arr, low, high, x):
    mid = (high + low) // 2
    
    # Check base case
    if high >= low:
 
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return arr
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return arr.append(x)


        
    # return arr.insert(high,x)
    
startTime  = time.time()
l= [1,1,7,9,1,2,2,3,3,4,5,6]
# l = [np.random.randint(101) for i in range(100000)]
tmp = []
tmp.append(l[0])
print(l)
for i in l:
    t =  binary_search(tmp,0,len(tmp)-1,i)
    if t != None:
        tmp = t.copy()
print(tmp)
print(time.time() - startTime)
 