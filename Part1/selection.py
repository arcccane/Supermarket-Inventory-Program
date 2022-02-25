# Cheung Kai Cun Ronald, 202670M , IT2153-02
def selectionSort(theSeq):
    n = len(theSeq)
    p = 0
    for i in range(n - 1):
        # Assume the ith element is the smallest.
        small = i
        p += 1
        # Determine if any other element contains a smaller value.
        for j in range(i+1, n):
            if theSeq[j] < theSeq[small]:
                small = j
        # Swap the ith value and smallNdx value only if the smallest value is not already in its proper position.
        if small != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[small]
            theSeq[small] = tmp
            print('Pass',p,':',theSeq)
    return theSeq
