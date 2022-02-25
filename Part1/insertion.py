# Cheung Kai Cun Ronald, 202670M , IT2153-02
def insertionSort(theSeq):
    n = len(theSeq)
    p = 0
    for i in range(1,n):
        value = theSeq[i]
        pos = i
        p +=1
        while value > theSeq[pos-1] and pos>0:
            theSeq[pos] = theSeq[pos-1]
            pos-=1
        theSeq[pos] = value
        print('Pass',p,':',theSeq)
    return theSeq
