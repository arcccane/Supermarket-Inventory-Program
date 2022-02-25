# Cheung Kai Cun Ronald, 202670M , IT2153-02
import math
def binarySearch(theValues, target):
    low = 0
    high = len(theValues) - 1
    count = 0
    print(theValues)
    while high>=low:
        mid = math.floor((high+low)/2)
        count += 1
        print("Pass {} low {} mid {} high {}".format(count,low,mid,high))
        if theValues[mid] == target:
            # return mid
            return "Found!"
        elif target < theValues[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return "Not found!"
