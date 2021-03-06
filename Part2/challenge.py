# Cheung Kai Cun Ronald, 202670M , IT2153-02

def algorithm(seq,z):
    seq2 = []
    n = len(seq)
    match = False
    for i in range(0, n):
        x = z - seq[i]
        if seq[i] > z:
            break
        if x in seq2:
            print('X = {}\nY = {}'.format(x,seq[i]))
            match = True
        seq2.append(seq[i])
        # print('Pass',i+1,seq2)
    if not match:
        print('X = not found\nY = not found')
        return False
    return True

# QUESTION

# This challenge question will test you on the design and implementation of an efficient algorithm to solve the following problem.

# Given the following:
# i.	A sequence of positive integers, SEQ,  sorted in strictly increasing order (i.e. all the integers are distinct), and
# ii.	a positive integer Z

# Design and implement an algorithm with Python to check all pairs of integers X and Y in the sorted sequence such that X + Y = Z.

# (NOTE: A brute-force algorithm that compares all possible pairs in the sorted sequence and check if they sum up to equal to Z will work. However, using this approach will only give you a minimal score.)

# For example, if SEQ and Z are provided to your program as follow:

# SEQ:
# 2	3	5	7	8	10	15	16	23	28

# Z: 21

# Then, your Python program should return:
# •	X = 5
# •	Y = 16
# •	TRUE (since 5 + 16 = 21)


# However, if SEQ and Z are provided to your program as follow:

# SEQ:
# 2	3	5	7	8	10	15	16	23	28

# Z: 3

# Then, your Python program should return:
# •	X = not found
# •	Y = not found
# •	FALSE (since there does not exist two integers X and Y in SEQ, where  sum of X and Y = Z)


# SOLUTION

# theseq = [2,3,5,7,8,10,15,16,23,28]
# z_value = 21
# algorithm(theseq,z_value)

# x+y=z
# x=z-y
#

# for every element in seq
# x = z - element
# check if x is in seq2 (if x is in list, means a previous seq[i] + current seq[i] = z)
# if not then append element to list2
# if yes print found then append element to seq2
# repeat till end of seq
# end of loop, if never print anything print not found

# stop if element > z

# pass1  i=0 x=21-2 x=19 s2=[2]
# pass2  i=1 x=21-3 x=18 s2=[2,3]
# pass3  i=2 x=21-5 x=16 s2=[2,3,5]
# pass4  i=3 x=21-7 x=14 s2=[2,3,5,7]
# pass5  i=4 x=21-8 x=13 s2=[2,3,5,7,8]
# pass6  i=5 x=21-10 x=11 s2=[2,3,5,7,8,10]
# pass7  i=6 x=21-15 x=6 s2=[2,3,5,7,8,10,15]
# pass8  i=7 x=21-16 x=5  x in s2 = TRUE    s2=[2,3,5,7,8,10,15,16]

# compare x value with the prev pass s2
