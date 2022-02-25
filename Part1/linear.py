# Cheung Kai Cun Ronald, 202670M , IT2153-02
def sequentialSearch(theValues, target):
    n = len(theValues)
    print(theValues)
    for i in range(n):
        print(i+1,"Pass(s)")
        if theValues[i] == target:
            return "Found!"
        elif theValues[i] > target:
            return "Not found!"
    return "Not found!"

