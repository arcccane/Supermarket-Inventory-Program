# Cheung Kai Cun Ronald, 202670M , IT2153-02
def bubbleSort(theSeq):
    n = len(theSeq)
    p = 0
    # Perform n-1 times on sequence
    for i in range(n - 1, 0, -1):
        p += 1
        swp = False
        # Bubble the largest item to the end
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
                # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                swp = True
        print('Pass', p, ':', theSeq)
        if not swp:
            print('Items already sorted!')
            return theSeq
    return theSeq

